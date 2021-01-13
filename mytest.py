import csv
#./csiro/rawfixation/P1.csv

with open('./csiro/rawfixation/P1.csv') as fd:
    reader = csv.reader(fd)
    for idx, row in enumerate(reader):
        print('idx ', idx, ' row ', row)
        if idx > 5:
            break


