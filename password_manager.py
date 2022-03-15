# Password Manager
from cryptography.fernet import Fernet


master_pwd = input("What is the Master Password? ")

# Write Enc Key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #rstrip is used to remove the \n line break 
            user, passw = data.split("|") # this will split the data or the line(w/o \n) into 2 - user, passw
            print("User: ", user, "| Pass:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

# 'a' is the mode 'w' - overwrite the file with new data 'a' - add to the end of file, and creates one if its not there 'r' - read only
    with open('passwords.txt', 'a') as f:  # file = open('filename.txt') - opens a file.close('filename.txt') - closes
        f.write(name + "|" + pwd + "\n")        # using with bc it will close the file for you
                                        #as f is naming it all f

while True:
    mode = input("Add a New Password? or View Existing Password? Or Type Q to Quit. (add or view) ").lower()
    if mode in ["q", "quit"]:
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Input...")
        continue
