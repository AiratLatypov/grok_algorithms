def find_smallest(arr):
    # берем минимальное значение списка и его индекс
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        # в цикле проходимся по каждому индексу начиная с 1
        if arr[i] < smallest:
            # если значения от индекса будет меньше, то считаем его за минимальное значение
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    new_arr = []

    for _ in range(len(arr)):
        # в цикле проходимся по всем индексам
        # при каждом обходе находим наименьший элемент, удаляем его из изначального списка
        # и добавляем в новый массив
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))

    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))
