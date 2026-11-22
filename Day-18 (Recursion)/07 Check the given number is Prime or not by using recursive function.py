def prime(n,i = 2):
    if n <= 1:
        return "Not a prime number"
    elif i == n:
        return "Prime Number"
    elif n % i == 0:
        return "Not a prime number"
    else:
        return prime(n,i+1)
n = int(input("emter a number:"))
print(prime(n))