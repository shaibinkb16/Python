fruits={'Apple':2,'Orange':14,'Pinapple':31,'Watermelon':61,'Grapes':10}
x=list(fruits.items())
x.sort()
print("Ascending order is :",x)


x.sort(reverse=True)
print("Descending order is :",x)