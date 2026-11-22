class BankAccount:
    def name(self,name):
        self.name = name
        print(f"Account holder name : {name}")

    def initial_balance(self,amount):
        self.balance = amount
        print(f"initial amount : {amount}")

    def deposit(self,amount):
        self.balance += amount
        print(f"deposit amount :{amount}")

    def withdrawal(self, amount):
        if amount <= self.balance:          
            self.balance -= amount
            print(f"withdrawal amount : {amount}")
        else:
            print("insufficient balance")
    def check_balance(self):

        print(f"Available amount : {self.balance }")




n = input("enter account holder name :")
i = int(input("enter initial amount :"))
d = int(input("enter deposit amount :"))
w = int(input("enter withdrawal amount :"))


b = BankAccount()
b.name(n)
b.initial_balance(i)
b.deposit(d)
b.withdrawal(w)
b.check_balance()