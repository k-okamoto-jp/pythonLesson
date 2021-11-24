from email import message
import smtplib

# not work
smtp_host = 'smtp.gmail.com'
smtp_port = 465
from_email = 'saviola777jp@gmail.com'
to_email = 'saviola777jp@yahoo.co.jp'
username = 'saviola777jp@gmail.com'
password = 'viscabarca'

msg = message.EmailMessage()
msg.set_content('test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
