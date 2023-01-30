import hashlib
import os as tae
        
def update():
    tae.system('clear')
    name = input("Enter the account name to update: ")
    updated_pwd = input("Enter the new password: ")
    lines = []
    found = False
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            if user == name:
                lines.append(user + "|" + updated_pwd + "\n")
                found = True
            else:
                lines.append(user + "|" + pwd + "\n")

    with open("passwords.txt", "w") as f:
        f.writelines(lines)
    if not found:
        print("No account found with the name " + name)

def add():
    tae.system('clear')
    name = input('Account Name: ')
    pwd = input("Password: ")
    
    print(name,' is now added to the users, and your password is ',pwd,'\n\n\n don t share your password to anyone')

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

def delete():
    tae.system('clear')
    name = input("Account Name to delete: ")
    lines = []
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            if user != name:
                lines.append(user + "|" + pwd + "\n")

    with open("passwords.txt", "w") as f:
        f.writelines(lines)
        
def view():
     tae.system('clear')
     with open('passwords.txt', 'r') as bobo:
         for line in bobo.readlines():
             data = line.rstrip()
             values = data.split("|")
             if len(values) == 2:
                user,passwd = values
                print("\n\nUser:",user, "| Password:",passwd)
             else:
                print(f"Invalid line in file: {line}")       

def check_admin():
    with open("admin.txt", "r") as f:
        admin_hash = f.read().strip()
        
    username = input("Enter username: ")
    password = input("Enter password: ").encode('utf-8')
    password_hash = hashlib.sha256(password).hexdigest()
    
    if username == "admin" and password_hash == admin_hash:
        return True
    else:
        return False

while True:
    print('   \n\n PASSWORD MANAGER by CS\n')
    if check_admin():
        mode = input(
            "Would you like to add a new password or view existing ones\n \n(view, add,delete,update)\n type 'exit' if you want to quit::").lower()
            
        if mode == "q":
            break
        if mode == "view":
            view()
        elif mode == "add":
            add()
        elif mode == "delete":
            delete()
        elif mode == "update":
            update()
        elif mode == 'exit':
            tae.system('clear')
            print('\n\ndikana makakaalis dito beh!! syempre dapat q ang itype mo kung gusto mo mag exit, mwuaah!')
            continue
        else:
            tae.system('clear')
            print("Invalid mode.")
            continue
    else:
        print("Invalid admin creds!")
        continue
