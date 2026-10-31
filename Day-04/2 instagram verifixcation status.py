eligible_account = input()
meta_verified_subscription = input()
if eligible_account == "True":
    if meta_verified_subscription == "True":
        print("verified badge granted")
    else:
        print("None")
else:
    print("None")