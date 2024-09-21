import subprocess
import smtplib
from email.mime.text import MIMEText

def check_password_expiry(username):
    result = subprocess.run(['chage', '-l', username], capture_output=True, text=True)
    expiry_info = result.stdout
    if 'password must be changed in' in expiry_info:
        send_alert(f'Password Expiry for {username}', expiry_info)

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'admin@example.com'
    msg['To'] = 'user@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('admin@example.com', 'password')
        server.send_message(msg)

check_password_expiry('username')
