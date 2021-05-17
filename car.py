class Car:
    name="subaru"
    def __init__(self,model,colour):
        self.model=model
        self.colour=colour

    def sound(self):
        return  (f"iam {self.colour} subaru {self.model}")
    def want(self):
        return f"iam {self.model} model"
