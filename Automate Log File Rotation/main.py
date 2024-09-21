import os
import shutil
from datetime import datetime

def rotate_log(log_file):
    if os.path.exists(log_file):
        new_log_file = log_file + '-' + datetime.now().strftime('%Y-%m-%d')
        shutil.move(log_file, new_log_file)
        open(log_file, 'w').close()
        print(f"Rotated log file: {new_log_file}")

log_file = '/var/log/system.log'
rotate_log(log_file)
