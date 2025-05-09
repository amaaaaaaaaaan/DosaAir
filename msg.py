import requests
import mysql.connector

try:
    db = mysql.connector.connect(
        host='sql.freedb.tech',
        user='freedb_ranganshooja',
        database='freedb_dosair',
        password='Tu*U7mCup%6MH8K'
        # host='localhost',
        # user='root',
        # password='divya123',
        # database = 'dosair'
    )
    cu = db.cursor()
except:
    print('db not connected')
    db = ''

userdata = {'name' : 'Aman'}



readfeedlive()

