import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#TODO : сравнить средние баллы двух (мб и больше) видов кофе
file = 'coffee_ratings.csv'
coffee = pd.read_csv(file, delimiter=',')
new_coffee_list = coffee.rename(columns={'species': 'Виды_кофе','total_cup_points': 'Количество_очков' })

def average_points(length: int, sum_of_points: int):
    return sum_of_points // length


def min_points(lit_of_coffee):
    return lit_of_coffee.min()


def max_points(list_of_coffee):
    return list_of_coffee.max()


def statistics(length: int, type_of_coffee: str, list_of_coffee):
    print(f'Максимальное значение {type_of_coffee} {max_points(list_of_coffee["Количество_очков"])}')
    print(f'Минимальное значение {type_of_coffee} {min_points(list_of_coffee["Количество_очков"])}')
    print(f'Среднее значение {type_of_coffee} {average_points(length, list_of_coffee["Количество_очков"].sum())}')


def show_max_graph(max_robusta, max_arabica):
    plt.title('Максимальное')
    plt.xlabel('Виды кофе')
    plt.ylabel('Кол-во балов')

    robusta_list = ['Robusta']
    arabica_list = ['Arabica']
    plt.bar(robusta_list, np.float_(max_robusta), label='Robusta')
    plt.bar(arabica_list, np.float_(max_arabica), label='Arabica')


def show_min_graph(min_robusta, min_arabica):
    plt.title('Минимальное')
    plt.xlabel('Виды кофе')
    plt.ylabel('Кол-во балов')

    robusta_list = ['Robusta']
    arabica_list = ['Arabica']
    plt.bar(robusta_list, np.float_(min_robusta), label='Robusta')
    plt.bar(arabica_list, np.float_(min_arabica), label='Arabica')


def show_avg_graph(avg_robusta, avg_arabica):
    plt.title('Среднее')
    plt.xlabel('Виды кофе')
    plt.ylabel('Кол-во балов')

    robusta_list = ['Robusta']
    arabica_list = ['Arabica']
    plt.bar(robusta_list, np.float_(avg_robusta), label='Robusta')
    plt.bar(arabica_list, np.float_(avg_arabica), label='Arabica')


def show_graphs(max_robusta, max_arabica, min_robusta, min_arabica, avg_robusta, avg_arabica):
    plt.figure()

    plt.subplot(1, 3, 1)
    show_max_graph(max_robusta, max_arabica)
    plt.legend()

    plt.subplot(1, 3, 2)
    show_min_graph(min_robusta, min_arabica)
    plt.legend

    plt.subplot(1, 3, 3)
    show_avg_graph(avg_robusta, avg_arabica)
    plt.legend()

    plt.show()

def read_coffee_file(csv: str):
    print(f'Всего кофе {len(coffee)}')
    filterd_file = csv[['Количество_очков', 'Виды_кофе']]
    # Решено взять только 29, так как количество Робусты сильно меньше, чем Арабики.

    Arabica = filterd_file[filterd_file['Виды_кофе'] == 'Arabica'][:28]
    Robusta = filterd_file[filterd_file['Виды_кофе'] == 'Robusta']
    len_Arabica = len(Arabica)
    len_Rosuta = len(Robusta)

    statistics(len_Arabica, 'Arabica', Arabica)
    statistics(len_Rosuta, 'Robusta', Robusta)
    # show_max_graph(max_points(Robusta['Количество_очков']), max_points(Arabica['Количество_очков']))

    show_graphs(max_points(Robusta['Количество_очков']), max_points(Arabica['Количество_очков']), min_points(Robusta['Количество_очков']), min_points(Arabica['Количество_очков']), average_points(len_Rosuta, Robusta['Количество_очков'].sum()), average_points(len_Arabica, Arabica['Количество_очков'].sum()))

read_coffee_file(new_coffee_list)
