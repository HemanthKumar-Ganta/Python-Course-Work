l = list(map(str,input("enter strings :").split()))
d = { i : len(i) for i in l if i[0] in "AEIOUaeiou"}
print(d)