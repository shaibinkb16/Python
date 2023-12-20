a=str(input("Enter the String1 : "))
b=str(input("Enter the String2 : "))
print(a.replace(a[0], b[0]) +''+ b.replace(b[0],a[0]))