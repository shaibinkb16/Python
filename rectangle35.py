class rectangle:
    def __init__(self,l,b):
        self.l1=l
        self.b1=b
    def area(self):
        area1=self.l1*self.b1
        return area1
    def __lt__(self,obj):
        if(self.area()<obj.area()):
            return "The area of Rectangle1 is less than Rectangle2"
        else:
            return "The area of Rectangle2 is less than Rectangle1"
print("RECTANGLE 1")
l=int(input("Enter the length of  the recatngle1:"))5
6

b=int(input("Enter the breadth of the rectangle2:"))
obj1=rectangle(l,b)
print("The area is:")
print(obj1.area())
print("RECTANGLE 2")
l=int(input("Enter the length of the recrangle2:"))
b=int(input("Enter the breadth of the rectangle2:"))
obj2=rectangle(l,b)
print("The area is:")
print(obj2.area())
print("Now comparing the rectangles")
print(obj1<obj2)