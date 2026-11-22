def sub(n):
    if n == 0:
        return
    else:
        sub(n-1)
        print (2*n - 1 , end = " ")
n = int(input("enter a number :"))
print("Odd Numbers :" , end = "")
sub(n)