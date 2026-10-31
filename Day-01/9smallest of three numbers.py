s = int(input("enter the number:"))
s1 = int(input("enter the first number:"))
s2 = int(input("enter the second number:"))
if s<=s1 and s<=s2:
    print(s)
elif s1 <= s and s1 <= s2:
    print(s1)
elif s2 <= s and s2 <= s1:
    print(s2)
else:
    print("nothing")