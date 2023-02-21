import pandas as pd
import numpy as np

# file = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-07/coffee_ratings.csv'
#TODO : сравнить средние баллы двух (мб и больше) видов кофе
file = 'coffee_ratings.csv'
coffee = pd.read_csv(file, delimiter=',')
new_coffee_list = coffee.rename(columns={'species': 'Виды_кофе','total_cup_points': 'Количество_очков' })
# print(coffee[['total_cup_points', 'species']][:3])
# print(len(coffee))


def average_points(length: int, sum_of_points: int, type_of_cofffee: str):
    print(f'Средний бал кофе {type_of_cofffee} -', sum_of_points // length)
    return (sum_of_points // length)


def statistics(length: int, type_of_coffee: str, list_of_coffee):
    average_points(length, list_of_coffee['Количество_очков'].sum(), type_of_coffee)
    print(f'Минимальное значение {list_of_coffee["Количество_очков"].min()}')


def read_coffee_file(csv: str):
    print(f'Всего кофе {len(coffee)}')
    filterd_file = csv[['Количество_очков', 'Виды_кофе']]
    # Решено взять только 29, так как количество Робусты сильно меньше, чем Арабики.
    Arabica = filterd_file[filterd_file['Виды_кофе'] == 'Arabica'][:28]
    Robusta = filterd_file[filterd_file['Виды_кофе'] == 'Robusta']
    len_Arabica = len(Arabica)
    len_Rosuta = len(Robusta)
    statistics(len_Arabica, 'Arabica', Arabica)
    # average_points(len_Arabica, Arabica['Количество_очков'].sum(), 'Arabica')
    # average_points(len_Rosuta, Robusta['Количество_очков'].sum(), 'Robusta')

    print(Arabica)


read_coffee_file(new_coffee_list)