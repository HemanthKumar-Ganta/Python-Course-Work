n = list(map(str , input("enter names :").split()))
p = list(map(int,input("enter prices of fruits :").split()))
d = {i : j for i,j in zip(n,p) }
print(d)