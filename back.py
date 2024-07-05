import mysql.connector
import hashlib
db = mysql.connector.connect(
        host='sql.freedb.tech',
    user='freedb_ranganshooja',
    database='freedb_dosair',
    password='xxbJ!G46CXDsBuT'
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
           userdata['pass'] = ps
           print(ps , j )
           return us


def register(u,p,name, location, history):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(p.encode('utf-8'))
    hashed_password = sha256_hash.hexdigest()

    try:
        cursor.execute('INSERT INTO users (username, password, name, preferred_location, history) VALUES (%s, %s, %s, %s, %s)',
                        (u, hashed_password, name, location, history))
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return 'Something went wrong with the database operation.'
    else:
        return True

__all__ = ['confirmlogin' , 'register' , 'userdata']


def create_flights_table():
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
                            flight_id INT AUTO_INCREMENT PRIMARY KEY,
                            flight_number VARCHAR(20) NOT NULL,
                            departure_time DATETIME NOT NULL,
                            arrival_time DATETIME NOT NULL,
                            origin VARCHAR(50) NOT NULL,
                            destination VARCHAR(50) NOT NULL,
                            seats_available INT NOT NULL,
                            price DECIMAL(10, 2) NOT NULL
                            )''')
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error creating flights table: {err}")
        return 'Something went wrong with creating the flights table.'
    else:
        return True  
    finally:
        if db:
            db.close()
            cursor.close()  # to Close connections even on errors

