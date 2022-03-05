import csv
with open("file.csv",newline="")as file:
    data=csv.reader(file,delimiter=' ',quotechar='|')
    for row in data:
        print(','.join(row))