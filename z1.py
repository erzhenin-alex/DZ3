#Ерженин Алексадр ДПИ23-1с
import random

# Генерация массива случайных целых чисел
n = 10  # Размер массива
array = [random.randint(0, 100) for _ in range(n)]
print("Исходный массив:", array)

# Подсчет четных элементов на нечетных местах и нечетных элементов на четных местах
even_on_odd = sum(1 for i in range(n) if i % 2 == 1 and array[i] % 2 == 0)
odd_on_even = sum(1 for i in range(n) if i % 2 == 0 and array[i] % 2 == 1)

# Вывод информации о подсчетах
print("Четные на нечетных местах:", even_on_odd)
print("Нечетные на четных местах:", odd_on_even)

# Определение порядка сортировки
if even_on_odd > odd_on_even:
    ascending = True
else:
    ascending = False

# Реализация алгоритма сортировки слиянием
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Сортировка массива
if ascending:
    merge_sort(array)
else:
    merge_sort(array)
    array.reverse()

print("Отсортированный массив:", array)