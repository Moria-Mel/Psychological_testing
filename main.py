from Analyze import analyze
from Graphic import graphic

FILE = 'b919.csv'
MALE = True


if __name__ == '__main__':
    data = analyze(FILE, MALE)
    graphic(data[0], data[1])

