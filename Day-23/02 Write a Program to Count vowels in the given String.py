n = input("enter the string :")
count = 0
vowels = "aeiouAEIOU"
for i in n:
    if i in vowels:
        count += 1
print(count)
