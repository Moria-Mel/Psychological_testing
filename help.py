import csv


with open('results.csv', 'r', encoding='utf-8') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    dat = sorted(list(data))
with open('res.txt', 'w', encoding='utf-8') as file:
    for i in dat:
        file.write(','.join(i).replace(';', ',') + '\n')
