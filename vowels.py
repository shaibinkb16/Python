V=['a','e','i','o','u','A','E','I','O','U']
word=input("Enter the word : ")
s=[i for i in word if i in V]
print(s)