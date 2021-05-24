class BankAccount:
    
    def __init__(self,name,phoneNumber,loan):
        self.phoneNuber=phoneNumber
        self.balance=0
        self.name=name
        self.loan=loan
    def amount(self):
        return f"your amount is {self.balance}"
    def name(self):
        return f"{self.name} is a good bank"

    def showBalance(self):
        return f"Hello {self.name} ,your balance is {self.balance}"
    def deposit(self,amount):
        if amount<0:
            return f"hello {self.name} your balance is {self.balance}"
        else:
            self.balance+=amount
            return self.showBalance

    def withdraw(self,amount):
        if amount > self.balance:
            return "your balance is {self.balance} you cannot withdraw {amount}"
        else:
                self.balance==amount
                return self.showBalance()
    def addLoan(self,amount):
        return f"hello {self.name},you can add a loan of {amount-self.loan}"
    def payloan(self,amount):
        return f"you have a loan due of ksh {amount}"
               