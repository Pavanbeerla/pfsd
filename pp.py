import csv
 

with open('Book1.csv', mode ='r')as file:
   

    csv File = csv.reader(file)
 

    for lines in csvFile:
        print(lines)
