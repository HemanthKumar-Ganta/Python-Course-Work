class Car:
    def make(self,make):
        self.make = make
        print(f"enter make: {make}")
    def model(self,model):
        self.model = model
        print(f"enter model : {model}")
    def initial_speed(self,speed):
        self.speed = speed
        print(f"initial speed : {speed}")
    def acceleration(self,acc):
        self.speed+=acc
        print(f"acceleration speed:{acc}")
    def breaking(self,break1):
        if break1 <= self.speed:
            self.speed -= break1
            print(f"break speed : {break1}")
        else:
            self.speed = 0
    def apply(self):
        print(f"current speed : {self.speed}")

make = input("enter name of make :")
model = input("enter model name :")
i = float(input("enter initial speed :"))
a = float(input("enter acceleration speed :"))
b = float(input("enter break speed :"))
c = Car()
c.make(make)
c.model(model)
c.initial_speed(i)
c.acceleration(a)
c.breaking(b)
c.apply()
        