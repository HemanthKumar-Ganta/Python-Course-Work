def num(n):
    if n == 0:
        print(0 , end = "")
        return
    else:
        print(n,end="")
        num (n-1) 
        print(n,end = "")
n = int(input("enter a number :"))
num(n)