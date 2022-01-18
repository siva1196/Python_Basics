

class Calculation():

    def Add(self,a,b):
        self.a = a
        self.b  =b
        add = self.a + self.b
        return add
    def Substract(self,a,b):
        self.a = a
        self.b  =b
        sub = self.a - self.b
        return sub
    def Multiplication(self,a,b):
        self.a = a
        self.b  =b
        mul = self.a * self.b
        return mul
    def Division(self,a,b):
        self.a = a
        self.b  =b
        div = self.a / self.b
        return div

Calc = Calculation()

print("Addition",Calc.Add(5,6))
print("Subtraction",Calc.Substract(5,6))
print("Multiplication",Calc.Multiplication(5,6))
print("Division",Calc.Division(5,6))
