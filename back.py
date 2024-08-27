import csv
import json
import mysql.connector
import hashlib
import geocoder
import airportsdata
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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

def get_number_of_seats_booked():
    cu.execute(f"select count(seat_number) from seats_booked where status = 'bkd' and booking_id = {bkdFlight['booking_id']};")
    k = cu.fetchone()
    return int(k[0])

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
    userdata['name'] = u
    userdata['ploc'] = get_current_city()
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
    cu.execute(f'SELECT * FROM flights f,Schedule s WHERE s.fno = f.fno and  FromDest="{get_current_city()}" and new_date > "{date}"')
    x = cu.fetchall()
    for u, i in enumerate(x): #what does enumerate do ??? enumarate is unpacking the list of tuples and giving me just the value in i
        time = i[7]
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
            'date' : i[8],
            'time' : time,
            'booking_id' : i[10]
        }
        dic_lst.append(flight_dict)
    return dic_lst


def book(data):
    cu.execute(f'select * from flights f where f.Fno = {data["fno"]}') 
    i = cu.fetchone()
    print(i)
    global bkdFlight #stores the currently selected flight data
    bkdFlight = {
            "fno":i[0],
            "from":get_airport_code(i[1]) ,
            "to":get_airport_code(i[2]) ,
            "price": i[3],
            'duration': i[4],
            "time" : data['time'],
            "date" : data['date'],
            "booking_id" : data['booking_id']

    }
    print(bkdFlight)
    
def pullbooked():
    return bkdFlight

def carbon_emission():
    fno=bkdFlight['fno']
    cu.execute(f"select Distance from flights where fno={fno}")
    x=cu.fetchone()[0]
    no=get_number_of_seats_booked()
    em_fact=0.2
    em=int(x*(no/no+em_fact**100)*em_fact)
    return em
def no_trees():
    no=int(carbon_emission()*0.35)
    return no

def ticketcalc(catlover): #calculation to be done here
    #🐔🐔🐔👉👉👉👉👉 mr.aman go to bookings folder script.js file line 215🐈🐈
    global passengerDetails
    passengerDetails = catlover
    fn=bkdFlight["fno"]
    cu.execute(f"select Price from flights where Fno={fn}")
    f_price=cu.fetchone()[0]
    tiktprice=0
    try:
        for i in catlover:
            passprice = 0
            food_price=0
            st=['A1','B1','A2','B2']
            food_lst=i['food']
            food_price+=food_lst[1]
            age =i['ageGroup']
            seat=i['seat']
            bgg=i['bgg']
            if age=="Child":
                f_price=(f_price*50)/100
            elif age=="Senior Citizen":
                f_price=(f_price*80)/100
            if seat in st:
                f_price+=(f_price*10)/100
            if bgg=='premium':
                f_price+=(f_price*2)/100
            elif bgg=='premium plus':
                f_price+=(f_price*4)/100
            passprice = f_price + food_price
            i['indi_price'] = passprice
            tiktprice+=f_price+food_price
        bkdFlight['totalprice'] = tiktprice
        print(bkdFlight , passengerDetails)
        mailconfirmation(passengerDetails)
    except:
        return 'data-error'
    else:
        return 'all good'

def search(fro, to, date='none', date2='none'):
    dic_lst = []
    
    # Base query
    query = f'SELECT * FROM flights f, Schedule s WHERE s.fno = f.fno and FromDest="{fro}" and ToDest="{to}"'
    
    # Adjust query based on date and date2
    if date != 'none' and date2 == 'none':
        query += f' and new_date >= "{date}"'
    elif date != 'none' and date2 != 'none':
        query += f' and new_date >= "{date}"'
    
    # Execute the query
    cu.execute(query)
    x = cu.fetchall()

    # Process the results
    for i in x:
        time = i[7].split(':')
        time.pop()
        time = ":".join(time)
        
        flight_dict = {
            "Fno": i[0],
            "FromDest": get_airport_code(i[1]),
            "ToDest": get_airport_code(i[2]),
            "from": i[1],
            "to": i[2],
            "Price": i[3],
            'duration': i[4],
            'date': i[8],
            'time': time
        }
        dic_lst.append(flight_dict)
    
    # Check if a return flight (date2) is required
    if date != 'none' and date2 != 'none':
        query_return = f'SELECT * FROM flights f, Schedule s WHERE s.fno = f.fno and FromDest="{to}" and ToDest="{fro}" and new_date >= "{date2}"'
        
        cu.execute(query_return)
        x_return = cu.fetchall()

        for i in x_return:
            time = i[7].split(':')
            time.pop()
            time = ":".join(time)
            
            flight_dict = {
                "Fno": i[0],
                "FromDest": get_airport_code(i[1]),
                "ToDest": get_airport_code(i[2]),
                "from": i[1],
                "to": i[2],
                "Price": i[3],
                'duration': i[4],
                'date': i[8],
                'time': time,
                'booking_id': i[10]
            }
            dic_lst.append(flight_dict)
    
    return dic_lst


def check_seats():
    cu.execute(f"select seat_number from seats_booked where booking_id = {bkdFlight['booking_id']} and status = 'bkd'")
    seat_layout = cu.fetchall()
    return(seat_layout)


def seat(no):
    print(no , bkdFlight['booking_id'])
    cu.execute(f'select status from seats_booked  where seat_number="{no}" and booking_id = {bkdFlight["booking_id"]}')
    if_seat = cu.fetchone()
    if if_seat == None:
        cu.execute(f'insert into seats_booked values({bkdFlight["booking_id"]} , "{no}" , "bkd")')
        db.commit()
    else:
        print('sold')



def writeTicket():
    bkdFlight['passengerdetails'] = json.dumps(passengerDetails)
    l = bkdFlight.pop('booking_id')

    csv_file = f"{userdata['name']}.csv"

    with open(csv_file, mode='a', newline='') as file:
        fieldnames = bkdFlight.keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(bkdFlight)
    bkdFlight['booking_id'] = l

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

def orderdetails(details):
    data = {}
    try:
        for pas in details:
            data[pas['email']] = [pas['firstName'] , pas['indi_price'] , pas['ageGroup'] , pas['seat'] , pas['bgg'] , pas['food'][0]]
        return data
    except:
        print('Passenger-Detail Error')
        return None

def mailconfirmation(passdetails):
    mailingList = orderdetails (passdetails)
    print('waka' , passdetails)
    for to_email in mailingList:
        from_email = 'dosaairways@gmail.com'
        app_password = 'jxxv jzeq jpjw hiym'

        msg = MIMEMultipart('alternative')
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = "Booking Confirmation"
        html_content = f"""<center style="background-color: #ffffff;font-family:system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;" width="100%">
  <table
    id="m_6339926504336945311bodyTable"
    border="0"
    cellpadding="0"
    cellspacing="0"
    align="center"
    width="100%"
    style="margin: 0px auto; max-width: 600px !important"
  >
    <tbody style="max-width: 600px !important">
      <tr style="max-width: 600px !important">
        <td
          id="m_6339926504336945311bodyCell"
          align="center"
          valign="top"
          style="max-width: 600px !important"
        >
          <img
            src="https://media.discordapp.net/attachments/844436240447176724/1267539264032342056/image.png?ex=66a9276e&is=66a7d5ee&hm=d0fada2c0730b3a0eeb3c5f71762b43875d9e8e488218860aba6488e2b89ed1b&=&width=1102&height=1102"
            width="100%"
            style="
              filter: brightness(0);
              clear: both;
              max-width: 100px !important;
              width: 100%;
              display: block;
            "
            border="0"
            data-image-whitelisted=""
            class="CToWUd"
            data-bit="iit"
          />
          <table
            id="m_6339926504336945311templateContainer"
            bgcolor="#ffffff"
            border="0"
            cellpadding="0"
            cellspacing="0"
            style="max-width: 600px; width: 100%; table-layout: fixed"
          >
            <tbody>
              <tr>
                <td align="center" valign="top">
                  <table
                    id="m_6339926504336945311templateBody"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    width="100%"
                    style="max-width: 600px; table-layout: fixed"
                  >
                    <tbody>
                      <tr>
                        <td
                          colspan="5"
                          valign="top"
                          width="100%"
                          style="padding: 30px 5%; color: #ffffff ; background: rgb(29, 0, 57);"
                        >
                          <p
                            style="
                              max-width: 540px;
                              line-height: 26px;
                              font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                              font-size: 16px;
                              font-weight: normal;
                              text-align: left;
                              color: #ffffff;
                              font-style: normal;
                              margin-bottom: 12px;
                              margin-top: 0px;
                            "
                          ></p>
                          <div>Dear&nbsp;{mailingList[to_email][0]},</div>
                          <div><br /></div>
                          <div></div>
                          <div style="display: inline">
                            <p>We are writing to express our gratitude for the prompt booking confirmation. Your efficiency and attention to detail have made our travel arrangements seamless. We appreciate the clarity provided in the confirmation details, which gives us peace of mind as we prepare for our journey.</p>
                              <span>Regards,<span>&nbsp; </span></span>
                            </p>
                            <p><span>Your booking details are attached below</span></p>
                            <div>
                              <hr align="left" width="33%" />

                              <div>
                                <div id="m_6339926504336945311_com_1">
                                  <span
                                    ><a
                                      name="m_6339926504336945311__msocom_1"
                                      href="http://otis.avature.net/ltrk/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTExNzcsImhhc2giOiJjNTU3NWRhZDQ2MWU0MTc2NGU3MzU1MGNhNzAzYTMwMThhYjg0ZTgyNGFmYjg2NzI4NzllZTEzMDQ4NjU3ZGRhIn0.K6sWpOmSs5lxNMYaQG_OPMDiiXpujSkSYA7Q3vDRrM0"
                                      target="_blank"
                                      data-saferedirecturl="https://www.google.com/url?q=http://otis.avature.net/ltrk/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTExNzcsImhhc2giOiJjNTU3NWRhZDQ2MWU0MTc2NGU3MzU1MGNhNzAzYTMwMThhYjg0ZTgyNGFmYjg2NzI4NzllZTEzMDQ4NjU3ZGRhIn0.K6sWpOmSs5lxNMYaQG_OPMDiiXpujSkSYA7Q3vDRrM0&amp;source=gmail&amp;ust=1722019837051000&amp;usg=AOvVaw0cVQqO-SYinl_vhCWTnaIO"
                                    ></a
                                  ></span>

                                  <p><br /></p>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div></div>
                          <p></p>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <tr>
                <td align="left" valign="top">
                  <table
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    width="100%"
                    style="max-width: 600px; table-layout: fixed ; background:#4400b1;"
                  >
                    <tbody>
                      <tr style="text-align: center">
                        <td colspan="5">
                          <span style="
                              font-family: Arial, sans-serif;
                              font-size: 45px;
                              line-height: 50px;
                              font-weight: bold;
                              text-align: center;
                              color: rgb(255, 255, 255);
                              font-style: normal;
                              margin: 0px;
                            ">
                            Booking
                          </span>
                        </td>
                      </tr>
                      <tr style="text-align: center">
                        <td colspan="5">
                          <p style="
                              font-family: Arial, sans-serif;
                              font-size: 15px;
                              font-weight: bold;
                              text-align: center;
                              color: rgb(255, 255, 255);
                              font-style: normal;
                              margin-top: 0px;
                              line-height: 20px;
                            ">
                         </p>
                        </td>
                      </tr>
                      <tr style="text-align: center">
                        <td colspan="5">
                          <p style="
                              font-family: Arial, sans-serif;
                              font-size: 25px;
                              text-align: center;
                              color: rgb(255, 255, 255);
                              font-style: normal;
                              margin-top: 0px;
                              line-height: 40px;
                            ">
                            {mailingList[to_email][0]}
                          </p>
                        </td>
                      </tr>
                      <tr style="text-align: center;background: #210159; padding: 10px; border-radius: 15px;">
                        <td colspan="5" style="padding-top: 10px;">
                          <span style="
                              font-family: Arial, sans-serif;
                              font-size: 25px;
                              font-weight: bold;
                              text-align: center;
                              color: rgb(255, 255, 255);
                              font-style: normal;
                              margin-top: 0px;
                            ">
                            {bkdFlight['from']}
                          </span>
                         <span style="color: white; width: 10px;"> TO </span>
                          <span style="
                              font-family: Arial, sans-serif;
                              font-size: 25px;
                              font-weight: bold;
                              text-align: center;
                              color: rgb(255, 255, 255);
                              font-style: normal;
                              margin-top: 0px;
                            ">
                            {bkdFlight['to']}
                          </span>
                        </td>
                      </tr>
                      <tr style="text-align: center">
                        <td colspan="5" style="background: #210159; padding: 10px;">
                      
                            <span style="
                            font-family: Arial, sans-serif;
                            font-size: 15px;
                            text-align: center;
                            color: rgb(255, 255, 255);
                            font-style: normal;
                            margin-top: 0px;
                          ">{bkdFlight['fno']}</span>
                        </td>
                      </tr>
                      <tr style="text-align: center;">
                        <td colspan="5" style="padding: 10px;">
                          <table style="width: 100%; color: white; font-size: 15px; text-align: center;">
                            <tr>
                              <th style="font-size: 25px; font-weight: 800;">Time</th>
                              <th style="font-size: 25px; font-weight: 800;">Date</th>
                            </tr>
                            <tr>
                              <td style="font-weight: 500;">{bkdFlight['time']}</td>
                              <td style="font-weight: 500;">{bkdFlight['date']}</td>
                            </tr>
                          </table>
                          
                         
                          
                        </td>
                      </tr>
                      <tr style="text-align: center;background: #9f67ff; padding: 10px; border-radius: 15px;">
                        <td colspan="5" style="padding: 10px;">
                          <table style="width: 100%; color: white; font-size: 15px; text-align: center;">
                            <tr>
                              <th style="font-weight: 800;">Age Group</th>
                              <th style="font-weight: 800;">Seat</th>
                              <th style="font-weight: 800;">Baggage</th>
                              <th style="font-weight: 800;">Menu</th>
                            </tr>
                            <tr>
                              <td style="font-weight: 500;">{mailingList[to_email][2]}</td>
                              <td style="font-weight: 500;">{mailingList[to_email][3]}</td>
                              <td style="font-weight: 500;">{mailingList[to_email][4]}</td>
                              <td style="font-weight: 500;">{mailingList[to_email][5]}</td>
                            </tr>
                          </table>
                          
                         
                          
                        </td>
                      </tr>
                      <tr style="text-align: center;">
                        <td colspan="5" style="text-align: center; padding: 10px;"><button style="padding: 10px;border-radius: 10px;border: none;background: #27005f; color: white; font-size: 15px;width: 200px;font-weight:800;" onclick="this.innerHTML ='';print(); ">${mailingList[to_email][1]}</button></td>
                      </tr>
                      <tr style="text-align: center"></tr>
                      <tr style="text-align: center">
                        <td colspan="5">
                          <p
                            style="
                              line-height: 26px;
                              font-family: Arial, sans-serif;
                              font-size: 12px;
                              font-weight: normal;
                              text-align: center;
                              color: rgb(255, 255, 255);
                              font-style: normal;
                              margin-top: 0px;
                            "
                          >
                            <a
                              href="http://otis.avature.net/ltrk/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTExNzcsImhhc2giOiI2N2ViNzU4ZDAzMzk5NDA5ODQ4NzA1MjRjOTBlN2ZkOTlhNTg1NmE2MWEyODRmOTQ2NDE5MzgwY2NhNTRkZjEwIn0.DZ6xO77lEztXJwrSpWwdG2G0xUSzQSWFA6fw0jxr71c"
                              style="
                                text-decoration: none;
                                color: #cba052;
                                max-width: 80%;
                                height: auto !important;
                                width: 100% !important;
                                max-width: 100% !important;
                                min-width: 100% !important;
                                line-height: 26px;
                                font-family: Arial, sans-serif;
                                font-size: 12px;
                                font-weight: normal;
                                text-align: center;
                                color: rgb(255, 255, 255);
                                font-style: normal;
                                margin-top: 0px;
                              "
                              target="_blank"
                              data-saferedirecturl="https://www.google.com/url?q=http://otis.avature.net/ltrk/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTExNzcsImhhc2giOiI2N2ViNzU4ZDAzMzk5NDA5ODQ4NzA1MjRjOTBlN2ZkOTlhNTg1NmE2MWEyODRmOTQ2NDE5MzgwY2NhNTRkZjEwIn0.DZ6xO77lEztXJwrSpWwdG2G0xUSzQSWFA6fw0jxr71c&amp;source=gmail&amp;ust=1722019837051000&amp;usg=AOvVaw0nyyUpmfoBHk1PThccj4im"
                              >Privacy Notice</a
                            >
                            © 2024 MHDV. All rights reserved.
                          </p>
                        </td>
                      </tr>
                      <tr style="text-align: center">
                        <td colspan="5">
                          <center
                            style="background-color: #f4f4f4"
                            width="100%"
                          >
                            <table
                              role="presentation"
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              width="100%"
                              id="m_6339926504336945311bodyTable"
                              style="
                                max-width: 600px !important;
                                width: 100%;
                                background:#4400b1;                              "
                            >
                              <tbody>
                                <tr>
                                  <td
                                    align="center"
                                    valign="top"
                                    id="m_6339926504336945311bodyCell"
                                    style="
                                      padding-top: 0;
                                      max-width: 600px !important;
                                    "
                                  >
                                    <table
                                      role="presentation"
                                      border="0"
                                      cellpadding="0"
                                      cellspacing="0"
                                      width="100%"
                                      style="max-width: 600px !important"
                                    >
                                      <tbody>
                                        <tr>
                                          <td
                                            align="center"
                                            valign="top"
                                            style="max-width: 600px !important"
                                          >
                                            <table
                                              role="presentation"
                                              border="0"
                                              cellpadding="0"
                                              cellspacing="0"
                                              width="100%"
                                              style="
                                                max-width: 600px !important;
                                              "
                                            >
                                              <tbody>
                                                <tr>
                                                  <td
                                                    align="center"
                                                    valign="top"
                                                    width="100%"
                                                    style="
                                                      max-width: 600px !important;
                                                    "
                                                  >
                                                    <table
                                                      role="presentation"
                                                      border="0"
                                                      cellpadding="0"
                                                      cellspacing="0"
                                                      width="100%"
                                                      style="
background:#4400b1;                                                        max-width: 600px !important;
                                                      "
                                                    >
                                                      <tbody></tbody>
                                                    </table>
                                                  </td>
                                                </tr>
                                              </tbody>
                                            </table>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </center>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>

</center>

"""

        try:
            part = MIMEText(html_content, 'html')

            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            server.login(from_email, app_password)

            server.sendmail(from_email, to_email, msg.as_string())

            server.quit()
        except:
            print('mailing error')
# def readfeed():
#     with open('feed.csv') as f:
#         feeds = csv.reader(f)
#         return list(feeds)
# def writefeed(feeback):
#     with open('feed.csv' , 'a') as f:
#         feedw = csv.writer(f)
#         feedw.writerow([userdata['name'],feeback])

def readfeed():
    cu.execute('select * from feeds')
    feeds = cu.fetchall()
    return (feeds)

def writefeed(feed):
    cu.execute(f'insert into feeds values ("{userdata["name"]}" , "{feed}")')
    db.commit()

def getTop():
    airports = airportsdata.load("IATA")
    cu.execute(f'Select ToDest From flights where FromDest = "{userdata["ploc"]}"')
    fromdests = cu.fetchall()
    dest =[]
    for i in fromdests:
           l = ''
           for o,k in airports.items():
              if k['city'] == i[0]:
                l =  k['name']
           dest.append({'name' : i[0] , 'air' : l})
    return dest

def getDesc(dest):
    with open(f'public/dest-data/desc/{dest}.txt') as f:
        return f.read()
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



__all__ = ['confirmlogin' , 'register' , 'userdata' , 'mk_dict' , 'dosamenu' , 'pullbooked' , 'bkdFlight','ticketcalc','search' , 'readTicket' , 'readTicket' , 'writeTicket', 'seat' , 'check_seats']
