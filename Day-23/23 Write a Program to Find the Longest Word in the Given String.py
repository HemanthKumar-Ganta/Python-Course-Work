s = input("enter a string :").split()
l = ""
for i in s:
    if len(i) > len(l):
        l = i
print(l)
