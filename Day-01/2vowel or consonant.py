n = input("enter: ")
if n in "aeiouAEIOU":
    print("vowel")
elif n.isalpha() and len(n) == 1:
    print("consonant")
