import glob
import mysql.connector
import hashlib
import geocoder
import airportsdata

try: 

    db = mysql.connector.connect(
        host='sql.freedb.tech',
        user='freedb_ranganshooja',
        database='freedb_dosair',
        password='Tu*U7mCup%6MH8K'
        # host='localhost',
        # user='root',
        # password='divya123',
        # database = 'dosaair'
    )
    cu = db.cursor()
except:
    print('db not connected')
    db = ''


userdata ={}
bkdFlight = {}


def get_airport_code(city_name):
    airports = airportsdata.load("IATA")
    for code, airport in airports.items():
        if airport['city'].lower() == city_name.lower():
            return code
    return None


def get_current_city():
    g = geocoder.ip('me')
    city = g.city
    return 'Sharjah' #will change this after testing 🐈

def confirmlogin(cred,u):
    sha256_hash = hashlib.sha256()
    cu.execute('select * from Users')
    k = cu.fetchall()
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
           userdata['ploc'] = get_current_city()
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
        cu.execute(f'insert into Users (Name , Pass) values("{u}" , "{l}")')
        db.commit()
    except:
        return 'something wrong with connection'
    else:
        return True
    
def mk_dict():
    dic_lst = []
    ca = "Sharjah" #is this line used ?
    cu.execute(f'SELECT * FROM flights f,Schedule s WHERE s.fno = f.fno and  FromDest="{get_current_city()}"')
    x = cu.fetchall()
    for u, i in enumerate(x):
        time = i[6]
        time = time.split(':')
        time.pop()
        time = ":".join(time)
        flight_dict = {
            "Fno":i[0],
            "FromDest":get_airport_code(i[1]) ,
            "ToDest":get_airport_code(i[2]) ,
            "from" : i[1],
            "to" : i[2],
            "Price": i[3],
            'duration': i[4],
            'date' : i[7],
            'time' : time
        }
        dic_lst.append(flight_dict)
    return dic_lst


def book(data):
    cu.execute(f'select * from flights where Fno = {data['fno']}') 
    i = cu.fetchone()
    global bkdFlight
    bkdFlight = {
        "fno":i[0],
            "from":get_airport_code(i[1]) ,
            "to":get_airport_code(i[2]) ,
            "price": i[3],
            'duration': i[4],
            "time" : data['time'],
            "date" : data['date']
    }
    
def pullbooked():
    return bkdFlight


nonvegdosa = [
    { "name": "Chicken Dosa", "price": 150 },
    { "name": "Mutton Keema Dosa", "price": 200 },
    { "name": "Egg Dosa", "price": 100 },
    { "name": "Pepper Chicken Dosa", "price": 170 },
    { "name": "Spicy Chicken Dosa", "price": 160 },
    { "name": "Chicken Tikka Dosa", "price": 190 },
    
]

vegdosa = [
    { "name": "Masala Dosa", "price": 80 },
    { "name": "Paneer Dosa", "price": 120 },
    { "name": "Mysore Masala Dosa", "price": 90 },
    { "name": "Cheese Dosa", "price": 110 },
    { "name": "Rava Dosa", "price": 70 },
        { "name": "Ghee Dosa", "price": 90 }

]

weirddosa = [
    { "name": "Chocolate Dosa", "price": 150 },
    { "name": "Avocado Dosa", "price": 180 },
    { "name": "Pineapple Dosa", "price": 160 },
    { "name": "Noodles Dosa", "price": 170 },
    { "name": "Paneer Tikka Dosa", "price": 200 },
    { "name": "Vegan Dosa", "price": 1200 }

]

dosamenu = [weirddosa , nonvegdosa , vegdosa]



__all__ = ['confirmlogin' , 'register' , 'userdata' , 'mk_dict' , 'dosamenu' , 'pullbooked' , 'bkdFlight']

