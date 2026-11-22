class Student:
    def name(self,name):
        print(f"Name of the student : {name}")
    def roll_number(self,roll_number):
        print(f"Student roll number : {roll_number}")
    def marks(self,marks):
        print(f"student marks : {marks}")
        average = sum(marks) / len(marks)
        print(f"average marks of the student is :{average}")
n = input("enter name of the student: ")
r = int(input("enter roll_number of the student :"))
m1 = float(input("enter marks of the student :"))
m2 = float(input("enter marks of the student :"))
m3 = float(input("enter marks of the student :"))
s = Student()
s.name(n)
s.roll_number(r)
s.marks([m1,m2,m3])