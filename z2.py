#Ерженин Алексадр ДПИ23-1с

import random

# Генерация массива случайных целых чисел
n = 10  # Размер массива
array = [random.randint(-20, 20) for _ in range(n)]
print("Исходный массив:", array)

# Проверка наличия отрицательных элементов
has_negative = any(x < 0 for x in array)

# Реализация сортировки вставками
def insertion_sort(array, ascending=True):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and ((ascending and array[j] > key) or (not ascending and array[j] < key)):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Сортировка массива
if has_negative:
    insertion_sort(array, ascending=True)  # По возрастанию
else:
    insertion_sort(array, ascending=False)  # По убыванию

print("Отсортированный массив:", array)