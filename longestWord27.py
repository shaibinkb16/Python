list=["hello","WOrld","shabin","shijo","sanu","sreekanth"]
print(list)
a=0
for i in list:
    a=len(i)if len(i)>a else a
print("Largest name is : ",i)
print("The length is : ",a)
