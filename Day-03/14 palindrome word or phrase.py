n = input("enter a name:")
n = n.replace(" ","").lower()
left = 0
right = len(n) -1
palindrome = True
while left <= right:
    if n[left] != n[right]:
        palindrome = False
        break
    left += 1
    right -= 1
if palindrome:
    print("palindrome")
else:
    print("not palindrome")


