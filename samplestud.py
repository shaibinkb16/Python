class student:
    def __init__(self,name,age,mark1,mark2,mark3):
        self.Name=name
        self.Age=age
        self.Mark1=mark1
        self.Mark2=mark2
        self.Mark3=mark3
    def total(self):
        self.Total=self.Mark1+self.Mark2+self.Mark3
    def display(self):
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("Total Mark=",self.Total)
name=input("Enter the name:")
age=int(input("Enter the age:"))
m1=int(input("Enter mark1:"))
m2=int(input("Enter mark2:"))
m3=int(input("Enter mark3:"))
obj1=student(name,age,m1,m2,m3)
obj1.total()
obj1.display()