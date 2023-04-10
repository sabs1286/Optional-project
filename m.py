import csv
with open('data.csv', 'r') as file:
    reader=csv.reader(file)
    for line in reader:
        print(line)