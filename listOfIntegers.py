list1=[1,2,6,43,56,73]
list2=[3,4,8,7,9,12,5]
print("List1 : ",list1)
print("List2 : ",list2)
print("Length of List1= ",len(list1))
print("Length of List2= ",len(list2))
if(len(list1)==len(list2)):
    print("length of list are same")
else:
    print("Not same length")
print("Sum of the list1 =",sum(list1))
print("Sum of list2= ",sum(list2))
if(sum(list1)==sum(list2)):
    print("Sum of two lists ar same")
else:
    print("Sum of twolist are diffrent")
check=any(item in list1 for item in list2)
print("Value occured in both lists :",check)
