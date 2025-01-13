
def binary_search(array: list, target: int) -> int | None:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = round((low + high) / 2)
        guess = array[mid]

        if guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
        elif guess == target:
            return mid


test_array = [1, 2, 5, 9, 10, 3, 7, 14, 11, 99]

print(binary_search(sorted(test_array), 9))  # 5
print(binary_search(sorted(test_array), 99))  # 9
print(binary_search(sorted(test_array), 7))  # 4
print(binary_search(sorted(test_array), -1))  # None
