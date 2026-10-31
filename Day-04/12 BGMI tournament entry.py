Registered = input("Enter registration status:")
fee = input("enter fee status:")
if Registered == "True":
    if fee == "True":
        print("Tournament entry confirmed")
    else:
        print("entry fee pending")
else:
    print("registration required")