from DataStructures.Heap import Heap


def heap_sort(arr):
    h = Heap()
    for i in arr:
        h.insert(i)
    return [h.remove() for _ in range(len(arr))]


if __name__ == "__main__":
    test_list = [2, 5, 25, 12, 123]
    print(heap_sort(test_list))
