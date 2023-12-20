n=int(input("Enter the number of elements :"))
a=[]
for i in range(0,n):
    c=int(input("Enter the elements: \n"))
    if(c>100):
        a.append("over")
    else:
        a.append(c)
print(a)