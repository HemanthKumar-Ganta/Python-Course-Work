def sum(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sum(n[1:])
n = list(map(int,input("enter numbers :").split()))
print("Total : ",sum(n))