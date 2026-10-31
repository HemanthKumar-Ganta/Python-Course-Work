n = int(input("enter budget:"))
if n > 10000:
    print("cloud hosting")
elif 5000 <= n <= 10000:
    print("business hosting")
elif 2000 <= n <= 50000:
    print("premium hosting")
else:
    print("single hosting")