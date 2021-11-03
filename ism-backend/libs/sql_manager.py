import pdb

from libs.config import *
from psycopg2.pool import SimpleConnectionPool

sql_pool = None

def get_sql_connection():
    global sql_pool

    if sql_pool is None:
        print('Initializing SQL DB connection pool')

        sql_pool = SimpleConnectionPool(
            minconn=1, maxconn=10,
            host=SQL_SERVER_ADDRESS, port=SQL_SERVER_PORT,
            dbname=SQL_DATABASE, user=SQL_USER_ID, password=SQL_USER_PW,
        )

    conn = sql_pool.getconn()

    return conn

# sql connection 돌려놓기
def put_sql_connection(conn):
    global sql_pool

    sql_pool.putconn(conn)

def execute_sql_query(query):
    conn = get_sql_connection()

    cursor = conn.cursor()
    cursor.execute(query)

    #title 주기
    rows = cursor.fetchall()
    cols = [x.name for x in cursor.description]

    buffer = []

    for row in rows:
        entry = { k:v for (k, v) in zip(cols, row) }
        buffer.append(entry)

    put_sql_connection(conn)

    return buffer
