n = list(map(int,input("enter a numbers :").split()))
element = int(input("enter the element"))
l = []
for i in range(len(n)):
    if n[i] == element:
        l.append(i)
print(l[-1])