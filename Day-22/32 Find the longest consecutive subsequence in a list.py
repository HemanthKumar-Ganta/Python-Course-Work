n = list(map(int,input("enter a number :").split()))
n.sort()
l = []
for i in range(len(n) - 1):
    if n[i+1] == n[i] +1:
        if n[i] not in l:

            l.append(n[i])
        if n[i+1] not in l:
            l.append(n[i+1])
print(l)