import csv
with open('test.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter = ',')
    next(readcsv)   # To remove the first row use : next(variable_name)
    for row in readcsv:
        print(row)
    line = csv_file.readlines()
    print(len(line))
    # for row in readcsv:
    #     print(row)

# 5 August, 2020

# Exercise : create csv file with states and capitals of each state, create csv file witg this data of India and read everything

# Exercise 2 : read all metro cities longitude and latitiude values in csv files

# Format { City name , longitude , latitude }