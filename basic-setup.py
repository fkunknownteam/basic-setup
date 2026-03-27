import os

os.system('clear')

print('Allow the Button For Access the Storage in Termux')
os.system('termux-setup-storage')

# Auto-handle all interactive prompts
os.environ['DEBIAN_FRONTEND'] = 'noninteractive'

cmds = [
    'apt update -y',
    'apt upgrade -o Dpkg::Options::="--force-confold" -y',  # <-- fixes openssl.cnf prompt
    'pkg update -y',
    'pkg upgrade -o Dpkg::Options::="--force-confold" -y',  # <-- fixes openssl.cnf prompt
    'pkg install git -y',
    'pkg install python -y',
    'pkg install python2 -y',
    'pkg install python3 -y',
    'pkg install curl -y',
    'pkg install zip -y',
    'pkg install php -y',
    'pkg install zsh -y',
    'pkg install ruby -y',
    'pkg install nano -y',
    'pkg install httping -y',
    'pkg install wget -y',
    'pkg install bash -y',
    'pkg install figlet -y',
    'pkg install openjdk-17 -y',
    'pip install --upgrade pip setuptools httpie',
    'pip install bs4 mechanize future',
    'pip2 install requests mechanize wget',
]

for cmd in cmds:
    os.system(f'DEBIAN_FRONTEND=noninteractive {cmd}')

os.system('clear')
os.system('cd && rm -rf basic-setup && cd $HOME')
