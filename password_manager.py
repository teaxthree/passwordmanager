hardcoded_user = "admin"
hardcoded_password = "password"

def login(username, password):
    if username == hardcoded_user and password == hardcoded_password:
        print("Login successful")
    else:
        print("Invalid username or password.")
        username = input("Username: ")
        password = input("Password: ")
    return username, password
    
#initial login prompt
user = input("Username: ")
pw = input("Password: ")


#continuously prompt for login until valid credentials are provided
while user != hardcoded_user or pw != hardcoded_password:
    login(user, pw)
     