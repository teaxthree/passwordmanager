hardcoded_user = "abc" #placeholder for authentication
hardcoded_password = "123" #placeholder for authentication
user = "" #input of username
pw = "" #input of password

def login(u, p):
    print("Invalid username or password.")
    u = input("Username: ")
    p = input("Password: ")
    return u, p
        
#initial login prompt
user = input("Username: ")
pw = input("Password: ")

#continuously prompt for login until valid credentials are provided
while user != hardcoded_user and pw != hardcoded_password:
    user, pw = login(user, pw)

print("Login successful.")

     