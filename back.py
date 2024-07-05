import mysql.connector
import hashlib
db = mysql.connector.connect(
        host='localhost',
    user='root',
    database='dosaair',
    password='divya123'
)

cursor = db.cursor()
userdata ={}

def confirmlogin(cred,u):
    sha256_hash = hashlib.sha256()
    cursor.execute('select * from users')
    k = cursor.fetchall()
    sha256_hash.update(cred.encode('utf-8'))
    j = sha256_hash.hexdigest()
    l = ''
    for i in range(len(j)):
        if i < len(u):
            l =l + j[i]+u[i]
        else:
            l= l+ j[i]
    for i in k :
       us = i[0]
       ps = i[1]
       if ps == l : 
           userdata['name'] = us
           print(ps , j )
           return us


def register(u,p) :
    sha256_hash = hashlib.sha256()
    print(u,p)
    sha256_hash.update(p.encode('utf-8'))
    p = sha256_hash.hexdigest()
    l = ''
    for i in range(len(p)):
        if i < len(u):
            l =l + p[i]+u[i]
        else:
            l= l+ p[i]
    print(l)
    try:
        cursor.execute(f'insert into users values("{u}" , "{l}")')
        db.commit()
    except:
        return 'something wrong with connection'
    else:
        return True

__all__ = ['confirmlogin' , 'register' , 'userdata']

