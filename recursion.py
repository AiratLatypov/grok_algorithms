def countdown(i):
    print(i)
    if i <= 1:
        # базовый случай
        return
    countdown(i - 1)


# функция факториала
def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


def sum_from_array(lst: list[int], i = 0):
    try:
        i += lst.pop(0)
        return sum_from_array(lst, i)
    except IndexError:
        return i


sorted([1,2,3])