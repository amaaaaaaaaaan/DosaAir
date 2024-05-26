import mysql.connector
db = mysql.connector.connect(
    host='sql7.freesqldatabase.com',
    user='sql7708896',
    database='sql7708896',
    password='xu8xNWxznn'
)


cursor = db.cursor()

def confirmlogin(cred):

    cursor.execute('select * from users')
    k = cursor.fetchall()
    for i in k :
       us = i[0]
       ps = i[1]
       if ps == cred : 
           return us
       

def register(u,p) :
    print(u,p)
    try:
        cursor.execute(f'insert into users values("{u}" , "{p}")')
        db.commit()
    except:
        return 'something wrong  connection'
    else:
        return True

__all__ = ['confirmlogin' , 'register']