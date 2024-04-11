import json
import argon2

#Password Hasher object
ph = argon2.PasswordHasher()

###FUNCTIONS###############################################################
def addPassword(): #application, username, password
    website = input("Application/Website: ").lower()
    username = input("Username: ")
    password = input("Password: ")

    #hashing password
    hash = ph.hash(password)
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
        "password": hash
    }
    data.append(new_entry)

    #write back to JSON file
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)


#continuously prompt for login until valid credentials are provided
def login():
    loginCounter = 3
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    #input username and password
    username = input("Username: ")
    password = input("Password: ")
    hash = ph.hash(password)
    print(hash)
    for entry in data:
        if entry["username"] == username and entry["password"] == hash and ph.verify("encrypted_password", password) == True:
            print(entry)
            return
        elif loginCounter == 0:
            print("Too many login attempts.")
            return
        else:
            print("Passwords did not match. Login attempts remaining: " + str(loginCounter))
            username = input("Username: ")
            password = input("Password: ")
        loginCounter -= 1
        

addPassword()        


