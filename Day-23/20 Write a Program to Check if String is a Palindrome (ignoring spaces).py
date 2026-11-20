s = input("enter a string :").replace(" ","")
left = 0
right = len(s) - 1
while left < right:
    if s[left] != s[right]:
        print("string is not a palindrome")
        break

    left += 1
    right -= 1
else:
    print("string is a palindrome")

