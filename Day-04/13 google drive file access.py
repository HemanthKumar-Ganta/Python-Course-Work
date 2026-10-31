n = input("enter link status:")
m = input("enter permission status:")
if n == "True":
    if m == "True":
        print("file opened successfully")
    else:
        print("access denied")
else:
    print("invalid file link")