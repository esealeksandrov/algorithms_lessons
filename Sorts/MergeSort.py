"""
Mergesor - сортировска слиянием.
1) Массив разбивается на две части. Если части по длинне больше чем 1,
рекурсивный вызов для каждой из частей, в противном случае возвращается сам список.
2) Выставляются два счетчика, каждый иуказывает на позицию в своем массиве.
3) сравниваются два числа из каждого списка , на которые указывают текущие счетчик.
4) То число, которое больше, вставляется в результирующий массив. А индекс стороны увеличивается на единиц
5) Если индекс одной из превысил длинну, результирующий массив заполняется полностью другой сторой
"""


def merge_sort(arr: list):
    left_index = 0
    right_index = 0
    len_arr = len(arr)
    if len_arr <= 1:
        return arr

    result = []
    left_arr = merge_sort(arr[:len_arr // 2])
    right_arr = merge_sort(arr[len_arr // 2:])
    left_arr_len = len(left_arr)
    right_arr_len = len(right_arr)

    while left_arr_len > left_index and right_arr_len > right_index:
        if left_arr[left_index] < right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1

    if left_arr_len > left_index:
        result.extend(left_arr[left_index:])
    elif right_arr_len > right_index:
        result.extend(right_arr[right_index:])

    return result


if __name__ == "__main__":
    import random
    from datetime import datetime
    import copy

    l = [random.randrange(0, 9999) for i in range(10)]
    l2 = copy.copy(l)
    l3 = copy.copy(l)
    print(l)
    start_t = datetime.now()
    print(merge_sort(l))
    print(datetime.now()-start_t)

    # start_t_2 = datetime.now()
    # l2 = l2.sort()
    # print(datetime.now() - start_t_2)
    #
    # start_t_3 = datetime.now()
    # mergeSort(l3)
    # print(datetime.now() - start_t_3)







