import csv
with open("csv3.csv", newline="") as csvfile:
    d = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i in d:
        print(','.join(i))
