import json
from cryptography.fernet import Fernet
import os
import base64

hardcoded_user = "abc" #placeholder for authentication
hardcoded_password = "123" #placeholder for authentication
user = "" #input of username
pw = "" #input of password
loginCounter = 3 #attempts remaining to input correct credentials


###FUNCTIONS###############################################################
def login(u, p): #username, password
    print("Invalid username or password.")
    u = input("Username: ")
    p = input("Password: ")
    return u, p

#generates key for password
def generate_key():
    return Fernet.generate_key()

def addPassword(): #application, username, password
    website = input("Application/Website: ")
    username = input("Username: ")
    password = input("Password: ")

    #object used for encrypting/decrypting key
    encrypted_password = cipher.encrypt(password.encode())
    #changing password from bytes to string using base64
    encrypted_password_str = base64.b64encode(encrypted_password).decode()
    #load existing JSON data
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    #add the new password entry
    new_entry = {
        "website": website,
        "username": username,
        "password": encrypted_password_str
    }
    data.append(new_entry)

    #write back to JSON file
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

#Generate encrpytion key only once when Python file starts
if "ENCRYPTION_KEY" not in os.environ:
    key = generate_key()
    os.environ["ENCRYPTION_KEY"] = key.decode()
key = os.environ["ENCRYPTION_KEY"]
cipher = Fernet(key)

print (key)
#initial login prompt
user = input("Username: ")
pw = input("Password: ")

#continuously prompt for login until valid credentials are provided
while user != hardcoded_user and pw != hardcoded_password and loginCounter != 0:
    print("Remaining login attempts: " + str(loginCounter))
    user, pw = login(user, pw)
    loginCounter -= 1

if (user == hardcoded_user) and (pw == hardcoded_password):
    print("Login successful.")
else:
    print("Login unsuccessful.")

addPassword()
