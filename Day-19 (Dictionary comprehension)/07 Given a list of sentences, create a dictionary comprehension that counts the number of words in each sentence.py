l = list(map(str,input("enter strings :").split(",")))
d = {i : len(i.split()) for i in l}
print(d)