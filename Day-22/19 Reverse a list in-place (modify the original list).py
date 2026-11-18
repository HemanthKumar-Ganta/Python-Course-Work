n = int(input("enter a size of list: "))
m = list(map(int,input("enter the elements of list: ").split()))
left = 0
right = len(m) - 1
while left < right:
    m[left] , m[right] = m[right] , m[left]
    left += 1
    right -= 1
print(m)