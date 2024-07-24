import eel 
import back 


eel.init('public')

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
def ticket(nambiar):
  return back.ticketcalc(nambiar)
  
@eel.expose
def regdata(u,p):
   if u != '' and p !='' :
      l = back.register(u,p)
      return l
   else:
      return 'Blank user and pass'
   
@eel.expose
def userdata():
  return back.userdata

@eel.expose
def smartRoutes():
  return back.mk_dict()

@eel.expose
def dosamenu ():
  return back.dosamenu

@eel.expose
def bookFlight(data):
  back.book(data)
  print(data)

@eel.expose
def bookedFlight():
  return back.bkdFlight

@eel.expose
def searchflight(fro , to ,date ):
  return back.search(fro , to , date)

@eel.expose
def searchroundflight(fro , to ,date , date2):
  return back.search(fro , to , date ,date2)

@eel.expose
def saveTicket():
  back.writeTicket()

@eel.expose
def pullTickets():
  return back.readTicket()

@eel.expose
def seatchange(no):
  back.seat(no)
@eel.expose
def checkon_seats():
  return back.check_seats()

eel.start('login.html' ,size=(1024, 768) )