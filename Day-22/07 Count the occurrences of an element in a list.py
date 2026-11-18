n = list(map(int,input("enter numbers: ").split()))
element = int(input("enter element :"))
count = 0
for i in range(len(n)):
    if n[i] == element:
        count += 1
print(count)