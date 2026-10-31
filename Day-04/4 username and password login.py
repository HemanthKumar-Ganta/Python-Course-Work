username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "admin123":
        print("Login successful")
    else:
        print("Invalid credentials")
else:
    print("Invalid credentials")

