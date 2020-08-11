import pymysql
from pymysql.cursors import DictCursor

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='info',
    charset='utf8mb4',
    cursorclass=DictCursor
)