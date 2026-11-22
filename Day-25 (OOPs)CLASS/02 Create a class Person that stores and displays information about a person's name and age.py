class Person:
    def name(self,name):
        print(f"name of the person: {name}")
    def age(self,age):
        print(f"age of the person: {age}")
name = input("enter name of the person :")
age = int(input("enter age of the person :"))
p =Person()
p.name(name)
p.age(age)