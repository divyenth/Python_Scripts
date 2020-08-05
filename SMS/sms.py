#pip install twilio before runing this code

from twilio.rest import Client 
 
account_sid = 'Your account sid' 
auth_token = 'Your account auth token' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='Number given by Twilio',  
                              body='message content',      
                              to='to number eg:+911234567890' 
                          ) 
 
print(message.sid)
