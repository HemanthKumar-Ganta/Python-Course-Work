n = list(map(int,input("enter numbers in a list :").split()))
element = int(input("enter element :"))
for i in range(len(n)):
    if n[i] == element:
       n.pop(i)
       break
print(n)
