l = list(map(int , input("enter numbers :").split()))
left = 0
right = len(l) -1
while left < right:
    if l[left] != l[right]:
        print("list is not a palindrome")
        break
    else:
        left += 1
        right -= 1
        print("list is palindrome")
        break
