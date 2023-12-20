lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
list=[i for i in range(lower,upper+1) if i**.5==int(i**.5)]
print(list)