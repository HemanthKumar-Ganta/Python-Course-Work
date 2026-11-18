n = list(map(int,input("enter a numbers :").split()))
elements = int(input("enter element :"))
for i in range(len(n)):
    if n[i] == elements:
        print(i) 
    
