n = int(input("enter the number:"))
total = 0
while n > 0:
    if n % 2 == 0:
        total = total + n
    n = n -1
print(total)
