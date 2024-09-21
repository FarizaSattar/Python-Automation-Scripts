import shutil
import smtplib
from email.mime.text import MIMEText

def check_disk_space(path='/'):
    total, used, free = shutil.disk_usage(path)
    percent_free = (free / total) * 100

    if percent_free < 20:
        send_email('Low Disk Space Alert', f'Disk space is below 20% ({percent_free:.2f}%)')

def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'admin@example.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('your_email@example.com', 'password')
        server.send_message(msg)

check_disk_space()
