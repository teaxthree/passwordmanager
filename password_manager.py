username = ""
password = ""
hardcoded_user = "admin"
hardcoded_password = "password"

def login():
    if username == hardcoded_user and password == hardcoded_password:
        print("Login successful")
    else:
        "Invalid username or password."
    username = input("Username: ")
    password = input("Password: ")

username = input("Username: ")
password = input("Password: ")

while username != hardcoded_user or password != hardcoded_password:
    login()
