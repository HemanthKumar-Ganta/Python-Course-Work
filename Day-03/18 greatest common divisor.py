n = int(input("enter a number: "))
n1 = int(input("enter another number: "))
i = min(n, n1)
while i > 0:
    if n % i == 0 and n1 % i == 0:
        print(i)
        break
    i -= 1
