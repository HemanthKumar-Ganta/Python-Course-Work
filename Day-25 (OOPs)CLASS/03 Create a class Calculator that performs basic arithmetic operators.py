class Calculator:
    def addition(self,a,b):
        print(f"Addition of a and b is :{a+b}")
    def subtraction(self,a,b):
        print(f"Subtraction of a and b is :{a-b}")
    def mul(self,a,b):
        print(f"Multiplication of a and b is :{a * b}")
    def div(self,a,b):
        if b != 0:           
            print(f"Division of a and b is :{a/b}")
        else:
            print("Cannot divide by zero")
a = int(input("enter the value of a :"))
b = int(input("enter the value of b :"))
c = Calculator()
c.addition(a,b)
c.subtraction(a,b)
c.mul(a,b)
c.div(a,b)