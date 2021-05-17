class BankAccount:
    name="equity"
    def __init__(self,branch,location,Account):
        self.branch=branch
        self.location=location
        self.Account=Account
    def message(self):
        return (f"This is equity bank ,{self.branch} ,{self.location} location  and your Bank account is {self.Account}")
    def datails(self):
        return ("This is {self.branch} branch")