
class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Print(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Child(Parent):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__(self.name, self.age)

child1 = Child("Siva", 25)
child1.Print()
