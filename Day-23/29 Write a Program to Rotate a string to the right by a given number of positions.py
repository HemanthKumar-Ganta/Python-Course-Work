s = input("enter a string :")
positions = int(input("enter no of c positions changed :"))
positions = positions % len(s)
s = s[-positions:] + s[:-positions]
print(s)