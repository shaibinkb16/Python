import csv
with open("csv3.csv",newline="")as csvfile:
    d=csv.DictReader(csvfile)
    print("Roll No,Student name")
    print(".................")
    for i in d:
        print(i['ROLLNO'], i['STUDENTNAME'])
