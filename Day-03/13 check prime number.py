n = int(input("Enter a number: "))
i = 2
if n <= 1:
    print("Not a prime number")
else:
    while i <= n:
        if n % i == 0:
            print("Not a prime number")
            break
        i = i + 1
    else:
        print("Prime number")

