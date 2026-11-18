n1 = list(map(int,input("enter elements :").split()))
n2 = list(map(int,input("enter elementss :").split()))

if len(n1) == len(n2):
    if n1 == n2:
        print("lists are equal")
    else:
        print("lists are not equal")
else:
    print("lists are not equal")
