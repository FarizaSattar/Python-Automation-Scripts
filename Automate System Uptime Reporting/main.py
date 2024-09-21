import os
import smtplib
from email.mime.text import MIMEText

def send_uptime_report():
    uptime = os.popen('uptime -p').read()
    send_email('System Uptime Report', uptime)

def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.send_message(msg)

send_uptime_report()
