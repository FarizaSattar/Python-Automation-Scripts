import subprocess

def install_packages(file_path):
    with open(file_path, 'r') as file:
        for package in file.readlines():
            package = package.strip()
            subprocess.run(['sudo', 'apt', 'install', '-y', package])
            print(f"Installed {package}")

packages_file = 'packages.txt'
install_packages(packages_file)
