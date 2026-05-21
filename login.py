username = input("Enter username: ")
password = input("Enter password: ")

query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

print("Executing Query:", query)

if username == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Login Failed")