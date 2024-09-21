import psutil
import smtplib
from email.mime.text import MIMEText

def send_alert(subject, message):
    sender = "your_email@example.com"
    receiver = "admin@example.com"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("your_email@example.com", "password")
        server.sendmail(sender, receiver, msg.as_string())

def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    if cpu_usage > 80:
        send_alert('High CPU Usage', f'CPU usage is at {cpu_usage}%')
    if memory_info.percent > 80:
        send_alert('High Memory Usage', f'Memory usage is at {memory_info.percent}%')
    if disk_usage.percent > 80:
        send_alert('Low Disk Space', f'Disk space usage is at {disk_usage.percent}%')

monitor_system()
