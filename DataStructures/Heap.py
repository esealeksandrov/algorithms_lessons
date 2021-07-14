"""
Куча - Бинарная структура данных в которой элементы соотносятся как родитель и два его потомка.
При этом основным свойством кучи является то, что родитель всегда меньше своих детей.
При добавлении в кучу нового элемента, н добавляется на самую последнюю позицию, и после меняется местами с родителем,
если был меньше него.
"""


class Heap:
    def __init__(self):
        self.list = []
        self.len = 0

    def insert(self, val):
        self.list.append(val)
        self.len += 1
        current_index = self.len - 1
        while current_index > 0 and self.list[current_index] < self.list[(current_index - 1) // 2]:
            parrent_index = (current_index - 1) // 2
            self.list[current_index], self.list[parrent_index] = self.list[parrent_index], self.list[current_index]
            current_index = parrent_index

    def remove(self):
        result = self.list[0]
        self.list[0], self.list[self.len-1] = self.list[self.len-1], self.list[0]
        del self.list[self.len-1]
        self.len -= 1
        current_index = 0
        while True:
            target_index = current_index
            left_son_index = 2 * current_index + 1
            right_son_index = 2 * current_index + 2
            if left_son_index < self.len and self.list[left_son_index] < self.list[target_index]:
                target_index = left_son_index
            if right_son_index < self.len and self.list[right_son_index] < self.list[target_index]:
                target_index = right_son_index
            if current_index == target_index:
                break
            self.list[current_index], self.list[target_index] = self.list[target_index], self.list[current_index]
            current_index = target_index
        return result
