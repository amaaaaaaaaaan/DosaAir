import mysql.connector
import hashlib
db = mysql.connector.connect(
        host='sql7.freesqldatabase.com',
    user='sql7711055',
    database='sql7711055',
    password='XGGTGnGcsQ'
)

cursor = db.cursor()
user ={}

def confirmlogin(cred):
    sha256_hash = hashlib.sha256()
    cursor.execute('select * from users')
    k = cursor.fetchall()
    sha256_hash.update(cred.encode('utf-8'))
    j = sha256_hash.hexdigest()
    for i in k :
       us = i[0]
       ps = i[1]
       if ps == j : 
           user['name'] = us
           user['pass'] = ps
           print(ps , j )
           return us


def register(u,p) :
    sha256_hash = hashlib.sha256()
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

