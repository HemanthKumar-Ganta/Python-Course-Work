age = int(input("enter the age:"))
income = int(input("enter the income:"))
if age < 18:
    print("you are underage")
else:
    if age >= 18:
        if income < 30000:
            print("your income is too low for a credit card")
        else:
            print("you are eligible for credit card")

