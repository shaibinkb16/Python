print("Area of Rctangle")
l=int(input("Length :"))
b=int(input("Breadth :"))
c=lambda x,y:x*y
print("Areaa of Rectangle :"+str(c(l,b)))
print("Area of square")
s=int(input("Side of square : "))
c=lambda x:x*x
print("Area of square:"+str(c(s)))
print("Area of triangle")
l=int(input("base : "))
b=int(input("height : "))
c=lambda x,y:.5*x*y
print("Area of triangle :"+str(c(l,b)))