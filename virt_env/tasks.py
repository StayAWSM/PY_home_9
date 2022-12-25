import random
import numpy
import sympy

# # 1. Вычислить число c заданной точностью d
# # Пример:
# # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
#
# num, acc = random.uniform(1, 10), random.randint(1, 10)
# print(f'Точность: {acc}')
# print(f'Ваше число: {round(num, acc)}')


# # 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# num = int(input('Введите число N: '))
# multi = [1]
# div = 2
# while num > 1:
#     if num % div == 0:
#         num /= div
#         if div not in multi:
#             multi.append(div)
#         div = 2
#     else:
#         div += 1
#
# print(multi)


# # 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
# lst = [random.randint(1, 20) for i in range(random.randint(4, 7))]
# print(f'Исходная последовательность: {lst}')
# li = numpy.unique(lst)
# print(f'Список уникальных значений: {li}')


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst

def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
coef = create_mn(k)
write_file(create_str(coef))


# # 5. Даны два файла, в каждом из которых находится запись многочлена.
# # Задача - сформировать файл, содержащий сумму многочленов.
#
# def get_polynom(file_num: int) -> str:
#     """Взять многочлен из файла"""
#     with open(f'file{file_num}.txt', 'r') as f:
#         polynom = f.readline()
#     return polynom
#
#
# """Сумма двух многочленов"""
# polynom1 = sympy.simplify(get_polynom(1))
# polynom2 = sympy.simplify(get_polynom(2))
# print('\t\t' + str(polynom1) + '\n\t\t' + str(polynom2))
# x = sympy.Symbol('x')
# polynom = str(sympy.simplify(polynom1 + polynom2))
# print('Сумма = ' + polynom)
# with open('file3.txt', 'w') as f:
#     f.write(polynom)