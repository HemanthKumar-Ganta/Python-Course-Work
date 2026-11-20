s = input("enter a string :")
for i in range(len(s)+1):
    for k in range(i):
        print(s[k], end = " ")
    print()