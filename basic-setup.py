import os
import shutil
import sys

def run(cmd):
    print(f"[+] {cmd}")
    return os.system(cmd)

def clear():
    os.system('clear')

clear()
print("[+]  (Allow storage permission)...")
run('termux-setup-storage')

run('xdg-open https://github.com/fkunknownteam')

os.environ['DEBIAN_FRONTEND'] = 'noninteractive'

# -------------------- System Packages --------------------
packages = [
    'apt update -y',
    'apt upgrade -y',
    'pkg install git -y',
    'pkg install python -y',
    'pkg install curl -y',
    'pkg install wget -y',
    'pkg install zip -y',
    'pkg install unzip -y',
    'pkg install tar -y',
    'pkg install php -y',
    'pkg install zsh -y',
    'pkg install nano -y',
    'pkg install vim -y',
    'pkg install bash -y',
    'pkg install figlet -y',
    'pkg install toilet -y',
    'pkg install neofetch -y',
    'pkg install htop -y',
    'pkg install openssl -y',
    'pkg install openjdk-17 -y',
    'pkg install termux-api -y'
]

# -------------------- Python Modules --------------------
pip_packages = [
    'pip install --upgrade pip setuptools wheel',
    'pip install requests',
    'pip install urllib3',
    'pip install bs4',
    'pip install mechanize',
    'pip install colorama',
    'pip install tqdm',
    'pip install flask',
    'pip install rich',
    'pip install httpie',
    'pip install pyfiglet',
    'pip install fake-useragent',
    'pip install dnspython'
]

# -------------------- Install System Packages --------------------
for cmd in packages:
    run(f'DEBIAN_FRONTEND=noninteractive {cmd}')

# -------------------- Install Python Packages --------------------
for cmd in pip_packages:
    run(cmd)
    
print("\n[+] Cleaning up setup folder...")

try:
    home = os.path.expanduser("~")
    
    os.chdir(home)
    
    folder_name = "basic-setup"
    folder_path = os.path.join(home, folder_name)

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"[✓] Removed: {folder_path}")
    else:
        print("[!] Folder not found, skipping...")

except Exception as e:
    print(f"[!] Cleanup error: {e}")

clear()
print("""
███████╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
█████╗  ███████╗   ██║   ██║   ██║██████╔╝
██╔══╝  ╚════██║   ██║   ██║   ██║██╔═══╝ 
███████╗███████║   ██║   ╚██████╔╝██║     
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
""")

print("[✓] Termux Setup Completed Successfully!")
print("[✓] Location:", os.getcwd())
