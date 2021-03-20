import csv


with open('res.csv', 'r', encoding='utf-8') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    dat = sorted(list(data))
keys = ['Г', 'Ц', 'Л', 'А', 'С', 'П', 'Ш', 'Э', 'И', 'Н', 'К', '?', '-', '*']
marks_dict = {i: [] for i in keys}
mot_dict = {i: [] for i in keys}
hours_dict = {i: [] for i in keys}


def add_to_dicts(name, i):
    marks_dict[name].append(float(i[1]))
    hours_dict[name].append(float(i[2]))
    mot_dict[name].append(float(i[3]))


for i in dat:
    if len(i) > 1:
        for j in i[-1]:
            add_to_dicts(j, i)
    else:
        add_to_dicts(i[-1], i)



print(marks_dict)
print(hours_dict)
print(mot_dict)