n = list(map(int,input("enter numbers :").split()))
for i in range(len(n)):
    for j in  range(len(n) - i -1):
        if n[j] > n[j+1]:
            n[j] , n[j+1] = n[j+1],n[j]
largest = n[-2]
print(largest)
