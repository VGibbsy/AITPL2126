import csv
with open('Lat and Long MCity.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter = ',')
    for row in readcsv:
        print(row[1:3])