from base64 import decode
from cryptography.fernet import Fernet

'''
# Write Enc Key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: # wb - write bytes mode
        key_file.write(key)
'''

# Load Key Function
def load_key():
    file = open("key.key", "rb") # rb - read bytes mode
    key = file.read()
    file.close()
    return key

# removed master password for now
# master_pwd = input("What is the Master Password? ")

key = load_key() #+ master_pwd.encode() # converts master password to bytes and adding it to key

#init encryption
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip() #rstrip is used to remove the \n line break 
            user, passw = data.split("|") # this will split the data or the line(w/o \n) into 2 - user, passw
            print("User: ", user, "| Pass:", fer.decrypt(passw.encode()).decode()) # will decrypt the encoded passw and decode to a normal string

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

# 'a' is the mode 'w' - overwrite the file with new data 'a' - add to the end of file, and creates one if its not there 'r' - read only
    with open('passwords.txt', 'a') as f:  # file = open('filename.txt') - opens a file.close('filename.txt') - closes
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")        # using with bc it will close the file for you
                                        # fer.encrypt encrypts it and pwd.encode changes it to bytes as above decode changes to normal string

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
