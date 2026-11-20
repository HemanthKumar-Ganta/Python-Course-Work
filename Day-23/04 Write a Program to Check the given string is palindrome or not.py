s = input("enter the string :")
left = 0
right = len(str) - 1
while left < right:
    if s[left] != s[right]:
        print("it's not a palindrome")
        break
    left += 1
    right -= 1
else:
    print("it is a palindrome")