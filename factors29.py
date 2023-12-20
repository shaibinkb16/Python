num=int(input("Enter the number : "))
list=[i for i in range (1,num+1)if num % i==0]
print("Factors of number=",list)