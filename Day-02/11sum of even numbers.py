n = int(input("Enter a number: "))
total = 0
for i in range(n+1):
    if i % 2 == 0:
        total += i
print(total)
