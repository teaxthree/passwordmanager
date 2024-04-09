hardcoded_user = "abc" #placeholder for authentication
hardcoded_password = "123" #placeholder for authentication
user = "" #input of username
pw = "" #input of password
loginCounter = 3 #attempts remaining to input correct credentials

def login(u, p):
    print("Invalid username or password.")
    u = input("Username: ")
    p = input("Password: ")
    return u, p
        
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
    print("Login unsuccessful")
