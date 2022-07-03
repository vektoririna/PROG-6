"""
    Автор: Моисеенко Павел, подгруппа № 2.

    ИСР 1.2. Задание: осуществить рефакторинг (модификацию) скрипта,
    вычисляющего статистические показатели для данных, считанных из
    CSV, с использованием библиотеки научных вычислений numpy.

"""


import csv
import numpy as np


def csv_reader(csv_file, col_num):
    reader = csv.reader(csv_file, delimiter=";")
    data = []
    for line in reader:
        data += [float(line[col_num - 1].replace(",", "."))]
    return data


def main():
    csv_path = "data.csv"
    column_number = 1
    with open(csv_path, newline="") as file:
        data = csv_reader(file, column_number)
    print("Среднее значение: ", np.mean(data))
    print("Дисперсия: ", np.var(data))
    print("Среднее квадратичное отклонение: ", np.std(data))


main()
