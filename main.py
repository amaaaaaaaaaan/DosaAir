import eel 
import back 
import geocoder
import airportsdata
eel.init('public')


def get_airport_code(city_name):
    print(city_name)
    airports = airportsdata.load("IATA")
    for code, airport in airports.items():
        if airport['city'].lower() == city_name.lower():
            return code
    return None


def get_current_city():
    g = geocoder.ip('me')
    city = g.city
    return city.split(' ')[0]




@eel.expose

def getdata(u,p):
   l =  back.confirmlogin(p,u)
   try :
      if l == u :
       return True
      else:
       return False
   except:
     return False
@eel.expose
def regdata(u,p):
   if u != '' and p !='' :
      l = back.register(u,p)
      return l
   else:
      return 'Blank user and pass'
   
@eel.expose
def userdata():
  back.userdata['ploc'] = get_current_city()
  return back.userdata

   

eel.start('login.html' ,size=(1114,654) )