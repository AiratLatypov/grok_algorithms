def quick_sort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # опорный элемент
    left_arr = []
    right_arr = []
    for elem in arr[1:]:
        if elem < pivot:
            left_arr.append(elem)
        elif elem > pivot:
            right_arr.append(elem)

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
