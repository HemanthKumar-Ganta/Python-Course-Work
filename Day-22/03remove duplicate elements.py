n = list(map(int,input("enter numbers: ").split()))
m = []
for i in n:
    if i not in m:
        m.append(i)
print(m)