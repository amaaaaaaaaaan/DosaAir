import mysql.connector
import hashlib
db = mysql.connector.connect(
        host='sql7.freesqldatabase.com',
    user='sql7708896',
    database='sql7708896',
    password='xu8xNWxznn'
)

sha256_hash = hashlib.sha256()
cursor = db.cursor()
user ={}

def confirmlogin(cred):

    cursor.execute('select * from users')
    k = cursor.fetchall()
    sha256_hash.update(cred.encode('utf-8'))
    j = sha256_hash.hexdigest()
    for i in k :
       print(j)
       us = i[0]
       ps = i[1]
       if ps == j : 
           user['name'] = us
           user['pass'] = ps
           return us


def register(u,p) :
    print(u,p)
    sha256_hash.update(p.encode('utf-8'))
    p = sha256_hash.hexdigest()
    try:
        cursor.execute(f'insert into users values("{u}" , "{p}")')
        db.commit()
    except:
        return 'something wrong  connection'
    else:
        return True

__all__ = ['confirmlogin' , 'register' , 'userdata']

