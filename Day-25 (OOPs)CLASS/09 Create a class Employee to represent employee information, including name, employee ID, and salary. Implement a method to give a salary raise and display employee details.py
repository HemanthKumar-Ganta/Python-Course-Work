class Employee:
    def set_name(self,name):
        self.name =name
        
    def set_employee_id(self,employee_id):
        self.employee_id = employee_id
        
    def set_salary(self,salary):
        self.salary=salary
        
    def set_raise(self,salary1):
        self.salary += salary1
        
    def display(self):
        print(f"Employee name is : {self.name}")
        print(f"Employee_id is : {self.employee_id}")
        
        print(f"Employee current salary is :{self.salary}")

n = input("enter employee name :")
i = int(input("enter employee id:"))
s = float(input("enter employee salary"))
r = float(input("enter employee raise salary:"))
e =Employee()
e.set_name(n)
e.set_employee_id(i)
e.set_salary(s)
e.set_raise(r)
e.display()





