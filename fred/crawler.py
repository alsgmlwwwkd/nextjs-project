import pdb
import json
import requests
import psycopg2
import psycopg2.extras
import datetime as dt
import time

from config import *

FRED_SERVER_ADDRESS = 'https://api.stlouisfed.org/fred'
SERIES_ID_LIST = ['DTB3', 'DTB6', 'DGS1', 'DGS2', 'DGS3', 'DGS5', 'DGS10', 'DGS20', 'DGS30']

def collect_series_info(series_id, cursor):
    print(f'Collecting series info of {series_id}')

    url = f'{FRED_SERVER_ADDRESS}/series?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json'
    # print(url)

    r = requests.get(url)
    # print(r.status_code)
    # print(r.text)

    data = json.loads(r.text) # json 형태
    data = data['seriess'][0]

    # print(data)

    query = f"""
        insert into fred_series_info (
            series_id, realtime_start, realtime_end, title, observation_start, observation_end, 
            frequency,  frequency_short, units,  units_short, seasonal_adjustment, seasonal_adjustment_short, 
            last_updated, popularity, notes
        ) values (
            '{series_id}',
            '{data['realtime_start']}',
            '{data['realtime_end']}',
            '{data['title']}',
            '{data['observation_start']}',
            '{data['observation_end']}',
            '{data['frequency']}',
            '{data['frequency_short']}',
            '{data['units']}',
            '{data['units_short']}',
            '{data['seasonal_adjustment']}',
            '{data['seasonal_adjustment_short']}',
            '{data['last_updated']}',
            '{data['popularity']}',
            '{data['notes']}'
        );
    """
    # print(query)
    # pdb.set_trace()
    cursor.execute(query)

# get last date data
def get_last_sample_date(series_id, cursor):
    query = f"""
        select max(date)
        from fred_series_values
        where series_id = '{series_id}'
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    last_date = rows[0][0]

    if last_date:
        return last_date.isoformat()
    else:
        return None

    #print(rows)
    #pdb.set_trace()



def collect_series_values(series_id, cursor):
    print(f'Collecting series values of {series_id}')

    url = f'{FRED_SERVER_ADDRESS}/series/observations?series_id={series_id}&api_key={FRED_API_KEY}&file_type=json'
    # print(url)

    last_date = get_last_sample_date(series_id, cursor)
    # if last_date exists
    if last_date:
        url += f'&observation_start={last_date}'


    r = requests.get(url)
    # print(r.status_code)
    # print(r.text)

    data = json.loads(r.text)

    query = """
        insert into fred_series_values (
            series_id, date, value
        )
        values %s
    """

    values = []

    for x in data['observations']:
        # 이미 있을 경우 넘기기
        if last_date and x['date'] <= last_date:
            continue

        try:
            value = float(x['value'])
        except:
            value = None

        item = (series_id, x['date'], value)
        # print(item)

        values.append(item)
        print(type(item))
        pdb.set_trace()

    if len(values) > 0:    
        psycopg2.extras.execute_values(cursor, query, values)



if __name__ == '__main__':
    sql_conn_str = f'host={SQL_SERVER_ADDRESS} port={SQL_SERVER_PORT} ' \
        f'dbname={SQL_DATABASE} user={SQL_USER_ID} password={SQL_USER_PW}'

    while True:
        now = dt.datetime.now().isoformat()
        print(f'[{now}] FRED crawler is starting...')
        
        # I/O = input/output
        with psycopg2.connect(sql_conn_str) as conn:
            cursor = conn.cursor()

            for series_id in SERIES_ID_LIST:
                # collect_series_info(series_id, cursor)
                collect_series_values(series_id, cursor)

                pass
            conn.commit()
        print('*** Completed!!! ***')
        print('Sleeping for one hour...')
        
        # 한 시간에 한 번 update
        time.sleep(60 * 60)
