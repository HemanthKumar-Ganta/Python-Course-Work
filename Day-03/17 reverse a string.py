n = input("enter a name:")
n = list(n)
left = 0
right = len(n)-1
while left < right:
    n[left], n[right] = n[right], n[left]
    left += 1
    right -= 1
print("".join(n))

