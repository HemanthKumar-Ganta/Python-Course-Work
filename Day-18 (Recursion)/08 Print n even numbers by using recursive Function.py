def even(n):
    if n == 0:
        return
    else:
        even(n-1)
        print(n * 2, end=",")

n = int(input("Enter a number: "))
print("Even numbers: ", end="")
even(n)