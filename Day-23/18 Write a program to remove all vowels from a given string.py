s = input("enter a string :")
ch = "AEIOUaeiou"
l = ""
for i in s:
    if i not in ch:
        l += i
print(l)