import csv
with open('C:\\Users\\Joseeustaquio\\Downloads\\ACOMPH.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
