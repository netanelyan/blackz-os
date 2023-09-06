from datetime import date
import time
from subprocess import call

print("""
██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗░░░░░░░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║░░░░░░██╔══██╗██╔════╝
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║█████╗██║░░██║╚█████╗░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║╚════╝██║░░██║░╚═══██╗
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║░░░░░░╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝░░░░░░░╚════╝░╚═════╝░
""")

with open('data/startup.data', 'r') as f:
    setup = f.read()



if setup == '0':
    print("[+] Welcome to Python-OS ! Lets set up your account")
    username = input("[?] Username? : ")
    with open('data/username.data', 'w') as f:
        f.write(username)
    password = input("[?] Password? : ")
    with open('data/password.data', 'w') as f:
        f.write(password)
    print("[+] Great! Restart your OS to login")
    with open('data/startup.data', 'w') as f:
        f.write('1')

if setup == '1':
    call(["python", "home.py"])

