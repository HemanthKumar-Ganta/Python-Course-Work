n = list(map(int,input("Enter the number: ").split()))
max = 0
for i in n:
    if i > max:
        max = i
print(max)