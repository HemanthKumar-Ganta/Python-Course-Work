n = input("enter a string: ")
rev = ""
for i in range(-1, -(len(n)+1), -1):
    rev = rev + n[i]
print(rev)