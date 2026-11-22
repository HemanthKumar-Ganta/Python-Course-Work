l = list(map(str,input("enter a list of strings :").split()))
d = {i : len(i) for i in l if len(i) % 2 == 0}
print(d)