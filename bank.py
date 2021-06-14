from datetime import datetime
class BankAccount:
    
    def __init__(self,name,phoneNumber,):
        self.phoneNuber=phoneNumber
        self.balance=0
        self.account=name
     
        self.statement=[]
    
    def amount(self):
        return f"your amount is {self.balance}"
    def name(self):
        return f"{self.name} is a good bank"

    def showBalance(self):
        return f"Hello {self.name} ,your balance is {self.balance}"
    def deposit(self,amount):
        try:
            10+amount
        except TypeError:
                    return f"The amount must be string"
           
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
        try:
            10+amount
        except TypeError:
                    return f"The amount must be string"
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
        try:
            10+amount
        except TypeError:
                    return f"The amount must be string"
        return f"you have a loan due of ksh {amount}"
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")
        return 
    def borrow(self,amount):
        try:
            10+amount
        except TypeError:
                    return f"The amount must be string"
        if amount<0:
            return "Your amount is too low"
        elif self.loan>0:
            return "you already have a loan"
        elif amount<0.1*self.balance:
            return "you are not qualified for the loan"    
        else:
            loan=amount*1.05
            self.loan=loan
            self.balance +=amount
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"you have borrowed"
            }
            self.statement.append(transaction)
            return "you have successfully borrowed loan"

    def repayloan(self,amount):
        try:
            10+amount
        except TypeError:
                    return f"The amount must be string"
        if amount<0:
            return "you cannot repay with that"
        elif amount<self.loan:
            self.loan-=amount
            return "you have qualifified for this loan"
        else:
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff)
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "narration":"you have repayed with this amount"
            }
            self.statement.append(transaction)
            return "you have successfully paid your loan"
    def transfer(self,BankAccount,amount):
        self.BankAccount=BankAccount
        self.amount=amount
        transactionfee=0.05*amount
        total=transactionfee+amount
        try:
            10+amount
        except TypeError:
                    return f"The amount must be in figures"
    
        if total>self.balance:
            return f"your balance is {self.balance} and you need at least {total} for this transfer"
        else:
            self.balance-=total
            BankAccount.deposit(amount)

class MobileMoneyAccount(BankAccount):
    def  __init__(self,name,phoneNumber,service_provider):
        BankAccount .__init__ (name,phoneNumber)
        self.service_provider=service_provider

    def buy_airtime(self,amount):
        try:
            10+amount
        except TypeError:
            return f"The amount must be in figures"
        if amount<0:
            return f"your amount is low to purchase this airtime"
        elif self.balance<amount:
            return f"your balance is low to purchase this amount of credit"
        else:
            self.balance-=amount
            return f"you have purchased airtime worth {amount}from {self.service_provider}.Your account balance is {self.balance}"

    

           


