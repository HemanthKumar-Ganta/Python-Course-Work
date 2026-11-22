l = list(map(int,input("enter a numbers :").split()))
s = {i for i in l if i > 0 and i % 2 == 0}
print(s)