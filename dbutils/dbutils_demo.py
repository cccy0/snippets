import pymysql
from DBUtils.PooledDB import PooledDB

pool=PooledDB(
    creator=pymysql,
    mincached=5,
    maxcached=50,
    host='192.168.98.143',
    user='root',
    passwd='123456',
    db='test'
)
conn=pool.dedicated_connection()
with conn.cursor() as cur:
    sql='show databases;'
    cur.execute(sql)
    rs=cur.fetchall()
# 此处断点 可在mysql shell中用 show processlist;查看五个已经建立的连接
print(rs)
# polldb适合频繁开关数据库连接的