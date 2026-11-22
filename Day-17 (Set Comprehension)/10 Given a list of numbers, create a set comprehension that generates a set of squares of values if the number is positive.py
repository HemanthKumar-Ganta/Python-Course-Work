n = list(map(int,input("enter numbers :").split()))
s = {i ** 2 for i in n if i > 0 }
print(s)