s = input("enter a string :").replace(" ","")
vowels = "AEIOUaeiou"
count = 0
for i in s:
    if i not in vowels:
        count += 1
print(count)