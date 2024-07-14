import csv
import json
import mysql.connector
import hashlib
import geocoder
import airportsdata
from datetime import datetime

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


userdata ={}
bkdFlight = {}
passengerDetails = []

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
    global userdata
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
    fieldnames = ['fno', 'from', 'to', 'price', 'duration', 'time', 'date', 'totalprice', 'passengerdetails']

    csv_file = f"{u}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

    try:
        cu.execute(f'insert into Users (Name , Pass) values("{u}" , "{l}")')
        db.commit()
    except:
        return 'something wrong with connection'
    else:
        return True
    
def mk_dict():
    today = datetime.today()
    date = today.strftime('%Y-%m-%d')
    dic_lst = []
    ca = "Sharjah" #is this line used ?
    cu.execute(f'SELECT * FROM flights f,Schedule s WHERE s.fno = f.fno and  FromDest="{get_current_city()}" and new_date >= "{date}"')
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
    cu.execute(f'select * from flights where Fno = {data["fno"]}') 
    i = cu.fetchone()
    global bkdFlight #stores the currently selected flight data
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

def ticketcalc(catlover): #calculation to be done here
    global passengerDetails
    passengerDetails = catlover
    fn=bkdFlight["fno"]
    cu.execute(f"select Price from flights where Fno={fn}")
    f_price=cu.fetchone()[0]
    age=""
    food_price=0
    tiktprice=0
    for i in catlover:
        food_lst=i['food']
        food_price+=food_lst[1]
        age+=i['ageGroup']
    if age=="Child":
        f_price=(f_price*50)/100
    elif age=="Senior Citizen":
        f_price=(f_price*80)/100
    tiktprice=f_price+food_price
    bkdFlight['totalprice'] = tiktprice
    print(bkdFlight , passengerDetails)
    return 'all good'


 

def search(fro  , to , date='none',date2 ='none'):
    dic_lst = []
    if date !='none' and date2 == 'none':  
        cu.execute(f'SELECT * FROM flights f,Schedule s WHERE s.fno = f.fno and  FromDest="{fro}" and ToDest ="{to}" and new_date >= "{date}"')
    elif date =='none' :
        cu.execute(f'SELECT * FROM flights f,Schedule s WHERE s.fno = f.fno and  FromDest="{fro}" and ToDest ="{to}"')
    elif date != 'none' and date2 !='none':
        cu.execute(f'SELECT * FROM flights f,Schedule s WHERE s.fno = f.fno and  FromDest="{fro}" and ToDest ="{to}" and new_date >= "{date}"')
        x = cu.fetchall()
        for i in x:
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
        cu.execute(f'SELECT * FROM flights f,Schedule s WHERE s.fno = f.fno and  FromDest="{to}" and ToDest ="{fro}" and new_date >= "{date2}"')
        x = cu.fetchall()
        for i in x:
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
            
    x = cu.fetchall()
    print(x)
    for i in x:
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


def writeTicket():
    bkdFlight['passengerdetails'] = json.dumps(passengerDetails)

    csv_file = f"{userdata['name']}.csv"

    with open(csv_file, mode='a', newline='') as file:
        # Determine the fieldnames from the bkdflight dictionary keys
        fieldnames = bkdFlight.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(bkdFlight)


def readTicket():
    csv_file = f"{userdata['name']}.csv"
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            try:
                row['passengerdetails'] = json.loads(row['passengerdetails'])
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON in row: {row}")
                print(f"Error details: {e}")
            data.append(row)
        return data

    
        # for row in reader:
        #     print({k: v for k, v in row.items() if k != 'passengerdetails'})
            
        #     passengerdetails = json.loads(row['passengerdetails'])
        #     for passenger in passengerdetails:
        #         print(passenger)


nonvegdosa = [
    { "name": "Chicken Dosa", "price": 1.83 },
    { "name": "Mutton Keema Dosa", "price": 2.44 },
    { "name": "Egg Dosa", "price": 1.22 },
    { "name": "Pepper Chicken Dosa", "price": 2.07 },
    { "name": "Spicy Chicken Dosa", "price": 1.95 },
    { "name": "Chicken Tikka Dosa", "price": 2.32 }
]

vegdosa =[
    { "name": "Masala Dosa", "price": 0.98 },
    { "name": "Paneer Dosa", "price": 1.46 },
    { "name": "Mysore Masala Dosa", "price": 1.10 },
    { "name": "Cheese Dosa", "price": 1.34 },
    { "name": "Rava Dosa", "price": 0.85 },
    { "name": "Ghee Dosa", "price": 1.10 }
]

weirddosa = [
    { "name": "Chocolate Dosa", "price": 1.83 },
    { "name": "Avocado Dosa", "price": 2.20 },
    { "name": "Pineapple Dosa", "price": 1.95 },
    { "name": "Noodles Dosa", "price": 2.07 },
    { "name": "Paneer Tikka Dosa", "price": 2.44 },
    { "name": "Vegan Dosa", "price": 14.63 }
]

dosamenu = [weirddosa , nonvegdosa , vegdosa]



__all__ = ['confirmlogin' , 'register' , 'userdata' , 'mk_dict' , 'dosamenu' , 'pullbooked' , 'bkdFlight','ticketcalc','search' , 'readTicket' , 'readTicket' , 'writeTicket']

