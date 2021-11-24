import pdb
import json
import datetime as dt

import requests

from dateutil.relativedelta import relativedelta
from urllib.parse import urlparse, parse_qs

from bs4 import BeautifulSoup
from config import *

def fetch_news_list(datestr, page):
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

        publisher = item.find("span", {"class": "writing"}).text

        if publisher is not None:
            publisher = publisher
        else:
            publisher = ''

        summary = item.find("span", {"class": "lede"}).text

        created_at = item.find("span", {"class": "date"}).text
        created_at = created_at.replace("오전", "AM").replace("오후", "PM")
        created_at = dt.datetime.strptime(created_at, "%Y.%m.%d. %p %I:%M")

        # print(title)
        # print(publisher)
        # print(created_at)
        # print(href)
        # print(summary)
        
        parsed_url = urlparse(href)
        qs = parse_qs(parsed_url.query)

        oid = qs['oid'][0]
        aid = qs['aid'][0]

        # 내부적으로 사용할 id
        news_id = 'nn-{}-{}'.format(oid, aid)

        # print(news_id)

        info = {
            'id': news_id,
            'title': title,
            'publisher': publisher,
            'created_at': created_at.isoformat(),
            'summary': summary,
            'href': href,
        }

        buffer.append(info)    
    
    return buffer

def fetch_news_list_for_date(date):
    # date 문자열로 바꿔줌
    datestr = date.strftime('%Y%m%d')

    print('[{}] Fetching news list on {}...'.format(
        dt.datetime.now(), datestr
    ))

    last_news_id = None

    for page in range(1, 1000):
        print('Fetching page {}...'.format(page))

        buffer = fetch_news_list(datestr, page)

        if last_news_id == buffer[-1]['id']:
            break
        else:
            last_news_id = buffer[-1]['id']

        upload_to_elastic_search(buffer)

        # 마지막 페이지 확인
        if len(buffer) < 20:
            break

        print(last_news_id)

    print('** Complete!! **')


def upload_to_elastic_search(buffer):
    if len(buffer) == 0:
        return

    data = ''

    for x in buffer:
        index = {
            'index': {
                '_id': x['id']
            }
        }
        data += json.dumps(index) + '\n'

        del x['id']

        data += json.dumps(x) + '\n'

        # print(data)
    

    headers = {
        'Content-Type': 'application/json'
    }
    # bulk insert    
    resp = requests.post(
        f'{ELASTICSEARCH_URL}/news/_bulk?pretty&refresh',
        headers=headers,
        data=data,
        auth=ELASTICSEARCH_AUTH
    )

    # print(resp.status_code)
    
    assert resp.status_code == 200



if __name__ == '__main__':
    base_date = dt.datetime(2021, 10, 25)

    for d in range(10):
        date = base_date + relativedelta(days=d)

        fetch_news_list_for_date(date)