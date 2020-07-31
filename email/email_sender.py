import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Felipe Alfonso'
email['to'] = 'tania.robayo96@gmail.com'
email['subject'] = 'Heeey You won 1,000,000 dollars!!'
# email['body'] = 'Here goes all what you want to write in mail'
email.set_content(html.substitute({'name': 'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('e-mail sender', 'password')
    smtp.send_message(email)
    print('all good boss!')
