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
  back.ticketcalc(nambiar)
  
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

  

eel.start('login.html' ,size=(1024, 768) )