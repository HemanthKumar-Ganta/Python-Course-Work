n = list(map(int,input("enter a numbers in list :").split()))
position = int(input("enter the position :"))
element = int(input("enter the element :"))
for i in range(position,len(n)):
    if n[i] == element:
        print(i)
        break