n = list(map(int,input("enter numbers :").split()))
l = []
for i in range(len(n)):
    if i % 2 != 0:
        l.append(n[i])
print(l)