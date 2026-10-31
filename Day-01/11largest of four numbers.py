s1 = int(input("enter first number"))
s2 = int(input("enter second number"))
s3 = int(input("enter third number"))
s4 = int(input("enter fourth number"))
if s1 >=s2 and s1 >= s3 and s1 >= s4:
    print(s1)
elif s2 >= s1 and s2 >= s3 and s2 >= s4:
    print(s2)
elif s3 >= s1 and s3 >= s2 and s3 >= s4:
    print(s3)
else:
    print(s4)