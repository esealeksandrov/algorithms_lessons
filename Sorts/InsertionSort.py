"""
InsertionSort - сортировка вставками.
1) В цикле перебираем i = 0..n-1 элементы массива
2) Для каждого iого элемента инициализируем цикл для перебора  j = n-1..0
3) Ищем позицию на которой i < j-1
4) Выходим из обоих циклов
"""


def insertion_sort(arr: list) -> list:
    arr_len = len(arr)
    for i in range(1, arr_len):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

def insertion_sort_2(arr: list) -> list:
    arr_len = len(arr)
    for i in range(1, arr_len):
        key = i
        for j in range(i, 0, -1):
            if arr[i] > arr[j]:
                key = j
        if key != i:
            arr[i], arr[key] = arr[key], arr[i]
    return arr


if __name__ == "__main__":
    from datetime import datetime as d
    from random import randint
    from copy import copy
    from MergeSort import merge_sort

    arr = [randint(0, 10000) for _ in range(0, 10000)]
    arr2 = copy(arr)
    print('start 1', arr)
    start_time = d.now()
    print(insertion_sort(arr))
    print(d.now()-start_time)
    print('start2', arr2)
    start_time_2 = d.now()
    print(insertion_sort_2(arr2))
    print(d.now() - start_time_2)

