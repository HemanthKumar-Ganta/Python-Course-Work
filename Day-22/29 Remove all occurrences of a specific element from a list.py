n = list(map(int,input("enter numbers in a list :").split()))
element = int(input("enter a element :"))
l =[]
for i in range(len(n)):
    if n[i] != element:
        l.append(n[i])
print(l)