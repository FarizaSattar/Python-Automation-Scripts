import csv
import os

def create_users_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            username = row[0]
            os.system(f'sudo useradd {username}')
            print(f"User {username} created")

csv_file = 'users.csv'
create_users_from_csv(csv_file)
