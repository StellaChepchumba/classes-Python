from datetime import datetime
class BankAccount:
    
    def __init__(self,name,phoneNumber,loan):
        self.phoneNuber=phoneNumber
        self.balance=0
        self.account=name
        self.loan=loan  
        self.statement=[]
    
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
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"you deposited"
            }
            self.statement.append(transaction)
           
    
    def withdraw(self,amount):
        if amount > self.balance:
            return f"your balance is {self.balance} you cannot withdraw {amount}"
        else:
                self.balance-=amount
                now=datetime.now()
                withdrawals={
                "amount":amount,
                "time":now,
                "narration":"you have withdrawn"
            }
                self.statement.append(withdrawals)
        return self.showBalance()

            
    def addLoan(self,amount):
        return f"hello {self.name},you can add a loan of {amount-self.loan}"
    def payloan(self,amount):
        return f"you have a loan due of ksh {amount}"
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")
        return 
               