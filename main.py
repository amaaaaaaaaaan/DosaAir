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
def regdata(u,p):
   if u != '' and p !='' :
      l = back.register(u,p)
      return l
   else:
      return 'Blank user and pass'
   

eel.start('login.html' ,size=(1114,654) )