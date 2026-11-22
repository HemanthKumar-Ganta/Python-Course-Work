n = list(map(str,input("enter strings :").split(",")))
d = {i.split("@")[0] : i.split("@")[1] for i in n}
print(d)