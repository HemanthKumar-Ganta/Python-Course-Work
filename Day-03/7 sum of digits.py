n = int(input("Enter a number: "))
total = 0
while n >0:
    s =n% 10
    total += s
    n //= 10
print(total)