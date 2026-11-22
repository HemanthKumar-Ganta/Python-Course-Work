n = int(input("enter a number :"))
d = {i : i ** 2 for i in range(1,n+1) if i % 3 == 0}
print(d)