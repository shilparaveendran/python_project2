class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.b-self.a
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.b/self.a
num = calculator(6,2)
print(num.add())
