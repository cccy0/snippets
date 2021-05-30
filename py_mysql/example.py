import pymysql

# Connect to the database
connection = pymysql.connect(host='192.168.98.132',
                             user='root',
                             password='123456',
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `test_table_1` (`name`) VALUES ( %s)"
        cursor.execute(sql, ("wocao",))
        cursor.executemany(sql, [("wocao",), ("wocao",), ("wocao",), ("wocao",)])

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `test_table_1` WHERE `name`=%s"
        cursor.execute(sql, ('wocao',))
        # 列信息
        print(cursor.description)
        result = cursor.fetchall()
        print(result)
