import pdb
import json
import datetime as dt
import psycopg2
import psycopg2.extras
import requests

from dateutil.relativedelta import relativedelta
from urllib.parse import urlparse, parse_qs

from bs4 import BeautifulSoup
from config import *

def fetch_news_list(datestr, page, cursor):
    # https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=101&date=20211120&page=3
    
    url = 'https://news.naver.com/main/list.naver' \
        '?mode=LSD&mid=sec&sid1=101&date={}&page={}'.format(datestr, page)
    # print(url)

    headers = { 
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' 
    }

    r = requests.get(url, headers=headers)

    # print(r.status_code)
    # print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')

    list_body = soup.find("div", {"class": "list_body"})

    buffer = []

    for item in list_body.find_all("li"):
        # print(item)

        link = item.find_all("a")[-1]
        title = link.text.strip()
        href = link['href']

        try:
            publisher = item.find("span", {"class": "writing"}).text

            if publisher is not None:
                publisher = publisher
            else:
                publisher = ''

            summary = item.find("span", {"class": "lede"}).text

            created_at = item.find("span", {"class": "date"}).text
            created_at = created_at.replace("오전", "AM").replace("오후", "PM")
            created_at = dt.datetime.strptime(created_at, "%Y.%m.%d. %p %I:%M")

            
            parsed_url = urlparse(href)
            qs = parse_qs(parsed_url.query)

            oid = qs['oid'][0]
            aid = qs['aid'][0]

            # 내부적으로 사용할 id
            news_id = 'nn-{}-{}'.format(oid, aid)

            info = (news_id, title, publisher, created_at.isoformat(), summary, href)

            # info = {
            #     'id': news_id,
            #     'title': title,
            #     'publisher': publisher,
            #     'created_at': created_at.isoformat(),
            #     'summary': summary,
            #     'href': href,
            # }

            # print(info)

            query = """
                insert into crawler_test (
                    news_id, title, publisher, created_at, summary, href
                )
                values %s
            """
            buffer.append(info)
        except:
            pass    
    psycopg2.extras.execute_values(cursor, query, buffer)
    
    return buffer

def fetch_news_list_for_date(date, cursor, num_pages=100):
    # date 문자열로 바꿔줌
    datestr = date.strftime('%Y%m%d')

    print('[{}] Fetching news list on {}...'.format(
        dt.datetime.now(), datestr
    ))

    last_news_id = None

    for page in range(1, num_pages):
        print('Fetching page {}...'.format(page))

        buffer = fetch_news_list(datestr, page, cursor)

        # if last_news_id == buffer[-1]['id']:
        #     break
        # else:
        #     last_news_id = buffer[-1]['id']

        # 마지막 페이지 확인
        if len(buffer) < 20:
            break

        print(last_news_id)

    print('** Complete!! **')



if __name__ == '__main__':
    sql_conn_str = f'host={SQL_SERVER_ADDRESS} port={SQL_SERVER_PORT} ' \
    f'dbname={SQL_DATABASE} user={SQL_USER_ID} password={SQL_USER_PW}'

    # 시작일과 끝나는 날짜 설정을 위해 추가
    base_date = dt.datetime(2021, 12, 1)
    end_date = dt.datetime(2021, 12, 8)
    
    date = base_date
    with psycopg2.connect(sql_conn_str) as conn:
        cursor = conn.cursor()

        while True:
            print(f'====================== Working on {date} ======================')
            fetch_news_list_for_date(date, cursor, num_pages=100)

            date += relativedelta(days=1)
            if date == end_date:
                break
        conn.commit()
