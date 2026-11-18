m1 = list(map(int,input("enter numbers :").split()))
m2 = list(map(int,input("enter numbers :").split()))
l = []
for i in m1:
    if i in m2:
        l.append(i)
print(l)
