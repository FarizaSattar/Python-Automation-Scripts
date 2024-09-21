import shutil
import os
from datetime import datetime

def backup_files(source, destination):
    today = datetime.now().strftime('%Y-%m-%d')
    backup_folder = os.path.join(destination, f'backup-{today}')
    shutil.copytree(source, backup_folder)
    print(f"Backup completed: {backup_folder}")

source_dir = '/path/to/important/files'
destination_dir = '/path/to/backup/location'

backup_files(source_dir, destination_dir)
