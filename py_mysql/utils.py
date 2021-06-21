import typing
from typing import Union

import pymysql
from traceback import print_exc
# Connect to the database 数据库已开启连接

connection = pymysql.connect(host='192.168.98.132',
                             user='root',
                             password='123456',
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def insert_data(data: Union[dict, typing.List[dict]]):
    if isinstance(data, dict):
        data = [data]
    # with connection: # second time already closed
    with connection.cursor() as cur:
        if data:
            columns = ','.join(data[0].keys())
            in_data=[list(i.values()) for i in data]
            placeholders = ",".join(["%s"] * len(data[0]))
            sql = "insert into %s (%s) values (%s)" % ('table_1', columns, placeholders)
            cur.executemany(sql, in_data)
    connection.commit()


if __name__ == '__main__':

    for i in range(2):
        try:
            insert_data([{"1": "2"}])
        except :

            print(print_exc())
