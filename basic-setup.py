import os
import shutil

# -------------------- CONFIG --------------------
APT_FIX = '-o Dpkg::Options::="--force-confold"'

# -------------------- UTILS --------------------
def run(cmd):
    print(f"[+] {cmd}")
    return os.system(cmd)

def run_apt(cmd):
    print(f"[APT] {cmd}")
    return os.system(f'DEBIAN_FRONTEND=noninteractive {cmd} {APT_FIX}')

def clear():
    os.system('clear')

# -------------------- START --------------------
clear()
print("[+] Allow storage permission...")
run('termux-setup-storage')

run('xdg-open https://github.com/fkunknownteam')

# -------------------- SYSTEM UPDATE --------------------
run_apt('apt update -y')
run_apt('apt upgrade -y')
run_apt('pkg update -y')
run_apt('pkg upgrade -y')

# -------------------- INSTALL PACKAGES --------------------
packages = [
    'git', 'python', 'curl', 'wget', 'zip', 'unzip', 'tar',
    'php', 'zsh', 'nano', 'vim', 'bash', 'figlet', 'toilet',
    'neofetch', 'htop', 'openssl', 'openjdk-17', 'termux-api'
]

for package in packages:
    run_apt(f'pkg install {package} -y')

# -------------------- PYTHON SETUP --------------------
pip_packages = [
    '--upgrade pip setuptools wheel',
    'requests', 'urllib3', 'bs4', 'mechanize',
    'colorama', 'tqdm', 'flask', 'rich',
    'httpie', 'pyfiglet', 'fake-useragent', 'dnspython'
]

for pkg in pip_packages:
    run(f'pip install {pkg}')

print("\n[+] Cleaning setup folder...")

home = os.path.expanduser("~")

folder_path = os.path.join(home, "basic-setup")

if os.path.exists(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"[✓] Removed: {folder_path}")
    except Exception as e:
        print(f"[!] Failed to remove folder: {e}")
else:
    print("[!] Folder not found, skipping...")

os.chdir(home)                 
os.system(f'cd {home}')

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
print(f"[✓] Current Path: {os.getcwd()}")   
