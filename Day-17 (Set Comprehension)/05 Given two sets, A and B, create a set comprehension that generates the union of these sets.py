a = set(map(int,input("enter values:").split()))
b = set(map(int,input("enter values :").split()))
s = {i for i in a | b}
print(s)