s = list(map(str,input("enter list of string :").split()))
l = list(map(int,input("enter ages :").split()))
d = {i : j for i , j in zip(s,l)}
print(d)