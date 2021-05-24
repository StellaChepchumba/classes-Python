class Student:
    school="AkiraChix"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
            return(f"my name is {self.name} and iam {self.age} years")
    def fullName(self):
            return (f"my full name is {self.name}")
    def __init__(self,first_name,last_name,age) :
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def greet(self,name):
        return f"hello{self.first_name},welcome to {self.school}"
    def year_of_birth(self):
        return f"Hello {self.first_name},you were born in {2021-self.age}"
    def initialise(self):
        return f"your initials are {self.first_name[0]} {self.last_name}"
        
   
   
   
   
   
   
   
    