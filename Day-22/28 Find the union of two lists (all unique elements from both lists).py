l1 = list(map(int,input("enter a numbers :").split()))
l2 = list(map(int,input("enter a numbers :").split()))
l = []
for i in l1:
    if i not in l:
        l.append(i)
for i in l2:
    if i not in l:
        l.append(i)
print(l)