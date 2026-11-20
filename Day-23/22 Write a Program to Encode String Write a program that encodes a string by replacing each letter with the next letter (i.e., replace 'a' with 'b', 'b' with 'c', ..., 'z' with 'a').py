s = input("Enter a string: ")
result = ""

for i in s:
    if i == "z":
        result += "a"
    elif i == "Z":
        result += "A"
    elif i.isalpha():
        result += chr(ord(i) + 1)
    else:
        result += i

print(result)