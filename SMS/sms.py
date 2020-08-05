#pip install twilio before runing this code

from twilio.rest import Client 
 
account_sid = 'AC17bd454b57bb250d4c8e4d1d5169c677' 
auth_token = '7451dfe0b564874f4da15e26b29bf199' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12056560905',  
                              body='haiii twilio ha some really good features..!',      
                              to='+919159029500' 
                          ) 
 
print(message.sid)