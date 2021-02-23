import csv
import json


def extra_points(bool, types, ito_dict):
    if bool:
        for type in types:
            ito_dict[type] += 1


def analyze(file, male):
    with open('Tests/' + file, 'r', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        res = [[i[0], i[1].split(), i[2].split()] for i in data]

    with open('Keys.json') as jsonfile:
        f = jsonfile.read()
        data = json.loads(f)

    V = 0
    keys_list = ['Г', 'Ц', 'Л', 'А', 'С', 'П', 'Ш', 'Э', 'И', 'Н', 'К', 'О',
                 'Д', 'Т', 'В', 'Е', 'd', 'М', 'Ф']
    ito_dict = {i: 0 for i in keys_list}
    for row in res:
        for answ in row[1]:
            try:
                for plus in data['Лучшие'][row[0]][str(answ)]:
                    if plus in ito_dict.keys():
                        ito_dict[plus] += 1
                    # print(row[0], answ, plus, '+')
            except Exception:
                print(row[0], answ, plus, '+', 'error')
        for answ in row[2]:
            try:
                for plus in data['Худшие'][row[0]][str(answ)]:
                    if plus in ito_dict.keys():
                        ito_dict[plus] += 1
                    #  print(row[0], answ, plus, '-')
            except Exception as error:
                print(error)
    for answ in res[5][1]:
        try:
            V += data['Алкоголизация']['Лучшие'][str(answ)]
        except KeyError:
            pass
    for answ in res[5][2]:
        try:
            V += data['Алкоголизация']['Худшие'][str(answ)]
        except KeyError:
            pass

    extra_points_dict = {ito_dict['Г'] <= 1: 'ПС', ito_dict['Ц'] >= 6: 'Л', ito_dict['А'] >= 4: 'Л',
                         ito_dict['П'] <= 1: 'Н', ito_dict['Н'] <= 1: 'П', ito_dict['К'] == 0: 'ШШИ',
                         ito_dict['К'] == 1: 'Ш', ito_dict['Д'] >= 6: 'Н',
                         ito_dict['Т'] > ito_dict['Д']: 'ППЦ',
                         ito_dict['В'] >= 6: 'ЭЭ', ito_dict['Е'] >= 6: 'ШИ', ito_dict['d'] >= 5: 'Ш',
                         ito_dict['О'] >= 6: 'С',
                         male and ito_dict['М'] < ito_dict['Ф']: 'СШИ', V <= -6: 'C', V >= 6: 'И'}
    for item in extra_points_dict.items():
        extra_points(item[0], item[1], ito_dict)
    return ito_dict, V