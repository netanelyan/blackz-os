from datetime import date
import time
from subprocess import call
import socket

with open('data/username.data', 'r') as f:
    username = f.read()
with open('data/password.data', 'r') as f:
    password = f.read()

logedin = False
while logedin is False:
    username_input = input("[?] Enter your username: ")
    password_input = input("[?] Enter your password: ")
    if username_input == username and password_input == password:
        logedin = True
    else:
        print("[+] Wrong username or password\n")

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print(f"\n[+] {d1}")
print(f"Welcome! {username}\n")

while True:
    print("""
[1] Open Web Browser
[2] Open Text Editor
[3] Open File Explorer
[4] Open Terminal
[5] Open BioS
[6] Close OS Safely
    """)
    choice = input("[?] Choose what you would like to do: ")

    if choice == '1':
        call(["python", "browser.py"])
    if choice == '2':
        call(["python", "texteditor.py"])
    if choice == '3':
        call(["python", "filebrowser.py"])
    if choice == '4':
        call(["python", "terminal.py"])
    if choice == '5':
        password_input = input(f"[?] Enter {username}'s password: ")
        if password_input != password:
                print("[+] Wrong username or password\n")
        else:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print(f"[1] Username: {username}")
            print(f"[2] Password: {password}")
            print(f"[+] Hostname: {hostname}")
            print(f"[+] Host IP: {IPAddr}")
            change = input(f"[?] Would you like to change your username or password? (1/2/no)")
            if change == "1":
                username = input("[?] What will be your username? : ")
                with open('data/username.data', 'w') as f:
                    f.write(username)
            elif change == '2':
                password = input("[?] What will be your password? : ")
                with open('data/password.data', 'w') as f:
                    f.write(password)
            else:
                print("Ok, shutting down the OS...")
                break
    if choice == '6':
        print("Shutting Down.")
        time.sleep(0.5)
        print("Shutting Down..")
        time.sleep(0.5)
        print("Shutting Down...")
        break