from webbrowser import get
import mysql.connector
from datetime import datetime,timedelta,time
import random

def generate_random_time():
    hour = random.randint(0, 23)
    minutes = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    minute = random.choice(minutes)
    second = 0
    return time(hour, minute, second)

def get_formatted_date(days_offset=0):

    today = datetime.now()
    
    target_date = today + timedelta(days=days_offset)
    
    formatted_date = target_date.strftime('%A %d %B')
    non_formatted_date = target_date.strftime('%Y-%m-%d')
    
    return formatted_date,non_formatted_date

n=3
_day,_date=get_formatted_date(n)# change n for how many days later from today the schedule has to be added

today=datetime.today().date()

db = mysql.connector.connect(
        host='sql.freedb.tech',
        user='freedb_ranganshooja',
        database='freedb_dosair',
        password='Tu*U7mCup%6MH8K')
cu=db.cursor()
cu.execute(f"select * from Schedule where new_date >'{today}'")
x=cu.fetchall()
l = 73
if x==[]:
    for i in range(10):
        fno=random.randint(1,10)
        random_time = generate_random_time()
        cu.execute(f"insert into Schedule values({fno},'{random_time}','{_day}','{_date}',{l})")
        db.commit()
        l+=1
    out=cu.fetchall()
# go to line 24 before running

