class Bank:
    def set_name(self,name):
        self.name = name
    def set_location(self,location):
        self.location = location
    def set_holders_names(self,holder_names):
        self.holder_names = holder_names
    def display(self):
        print(f"Bank name : {self.name}")
        print(f"Bank location : {self.location}")
        print(f"Account holders : {self.holder_names}")

n = input("enter bank name :")
l = input("enter location of the bank :")
s = int(input("enter size of the holder_names:"))
e = input("enter holder_names :")
b = Bank()
b.set_name(n)
b.set_location(l)
b.set_holders_names(s)
b.display()