import random
n = list(map(int,input().split()))
a =[]
b = []
for i in range(len(n)):
    if n[i] % 2 == 0:
        a.append(n[i])
    else:
        b.append(n[i])
random.shuffle(a)
random.shuffle(b)
c =[]
for i in range(len(a)):
    c.append(a[i])
    if i < len(b):
        c.append(b[i])
print(c)