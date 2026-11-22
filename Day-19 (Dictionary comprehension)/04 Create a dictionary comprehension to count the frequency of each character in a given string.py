s = input("enter a string :")
d = {i : s.count(i) for i in set(s)}
print(d)