n = list(map(int,input("enter numbers : ").split()))
n.sort()
print(n[0])
print(n[-1])




n= list(map(int,input("enter numbers : ").split()))
max = n[0]
min = n[0]
for i in n:
    if i > max:
        max = i
    else:
        min = i
print("maximum" , max)
print("minmum" , min)