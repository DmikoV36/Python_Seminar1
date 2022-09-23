# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

from random import randint
m = int(input("Введите количество строк массива: "))
n = int(input("Введите количество столбцов массива: "))
random_array = [[randint(10, 99) for j in range(n)] for i in range(m)]
list = [None for _ in range(m*n)]

def matrix_in_list (matrix):
    counter = 0
    for i in range(m): 
        for j in range(n):
            list[counter] = random_array[i][j]
            counter += 1
    return(list)


def sort_list(list):
    temp = 0
    for i in range(m*n):
        for j in range(m*n-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return(list)


def fill_matrix(matrix):
    counter = 0
    for i in range(m): 
        for j in range(n):
            random_array[i][j] = list[counter]
            counter += 1
    return(matrix)

def print_matrix(matrix):
    for i in range(m): 
        print(random_array[i])
        
print("Исходный массив случайных чисел")
print_matrix(random_array)
sort_list(matrix_in_list(random_array))
print("Отсортированный массив")
print_matrix(fill_matrix(random_array))