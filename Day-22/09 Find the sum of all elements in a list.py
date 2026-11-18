n = list(map(int,input("enter numbers :").split()))
total = 0
for i in range(len(n)):
    total += n[i]
print(total)