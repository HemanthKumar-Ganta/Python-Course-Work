s = list(map(str,input("enter names :").split()))
d = {i : len(i) for i in s if len(i) <= 5}
print(d)