from Analyze import analyze
from Graphic import graphic

FILE = 'test_res.csv'  # Имя файла
MALE = False  # Пол


if __name__ == '__main__':
    data = analyze(FILE, MALE)
    graphic(data[0], data[1])

