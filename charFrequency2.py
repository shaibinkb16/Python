list="Web programming using php"
newlist=[i for i in list.casefold()]
dict={}.fromkeys(newlist,0)
for i in list.casefold():
    if i in dict:
        dict[i]=dict[i]+1
print(list)
print(dict)