import random
import timeit

# 1 - Cортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднати менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
	# додати їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# 2 - Cортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# 3 - Timsort will be done by sorted function by Python

# Функція для генерації масиву
def generate_large_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# Функція для вимірювання часу сортування
def measure_sorting_time(sort_function, array):
    start_time = timeit.default_timer()
    sort_function(array)
    
    return timeit.default_timer() - start_time


# Розміри наборів даних
sizes = [100, 2000, 50000]

# Словник для зберігання результатів
results = {"Cортування злиттям": [], "Cортування вставками": [], "Сортування Timsort": []}

# Тестування алгоритмів
for size in sizes:
    array = generate_large_array(size)
    results["Cортування злиттям"].append(measure_sorting_time(merge_sort, array.copy()))
    results["Cортування вставками"].append(measure_sorting_time(insertion_sort, array.copy()))
    results["Сортування Timsort"].append(measure_sorting_time(sorted, array.copy()))

# Виведення результатів
for sort_type, times in results.items():
    print(f"{sort_type}:")
    for size, time in zip(sizes, times):
        print(f"   Розмір: {size}, Час: {time:.5f} сек.")
    print("\n")

"""
Отримані результати:

 Cортування злиттям:
   Розмір: 100, Час: 0.00010 сек.   
   Розмір: 2000, Час: 0.00226 сек.  
   Розмір: 50000, Час: 0.07808 сек. 


 Cортування вставками:
   Розмір: 100, Час: 0.00009 сек.   
   Розмір: 2000, Час: 0.04288 сек.  
   Розмір: 50000, Час: 27.63688 сек.


 Сортування Timsort:
   Розмір: 100, Час: 0.00001 сек.   
   Розмір: 2000, Час: 0.00016 сек.  
   Розмір: 50000, Час: 0.00568 сек. 

Висновок:
Абсолютний чемпіон за швидкістю - Timsort, навіть на досить великому наборі даних.
А от методи сортування злиттям та вставками показують велику швидкість лише на зовсім невеликих наборах даних. 
"""
