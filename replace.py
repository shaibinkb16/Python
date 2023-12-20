x = str(input('Enter a string : '))
first = x[0]
x = x.replace(first, '$')
x = first + x[1:]
print(x)