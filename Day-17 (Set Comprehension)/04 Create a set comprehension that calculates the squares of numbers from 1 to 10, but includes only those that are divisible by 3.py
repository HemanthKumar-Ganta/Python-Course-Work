n = int(input("enter a numbers :"))
s = { i**2 for i in range(1,n+1) if i ** 2 % 3 == 0 }
print(s)