s1 = input("enter a string :")
s2 = input("enter a string :")
s = sorted(s1)
t = sorted(s2)
if s == t:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")