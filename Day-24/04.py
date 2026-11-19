import random
n = input().split()
random.shuffle(n)
for i in range(0,len(n),2):
    print(n[i] , n[i+1])