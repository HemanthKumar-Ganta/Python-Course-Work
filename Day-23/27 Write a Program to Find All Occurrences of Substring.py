s = input("enter a string :")
substring = input("enter a substring :")
for i in range(len(s)):
    for j in range(len(substring)):
        if s[i:i+len(substring)] == substring:
            print(i)
            break