#run this script from terminal
#eg: python email.py

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()
email['from'] = 'sender name'
email['to'] = 'to mail address'
email['subject'] = 'Subject of email'

email.set_content('Write in email content here')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('From_mail address', 'password of from mail') #fill in details
    smtp.send_message(email)
    print('email sent')



