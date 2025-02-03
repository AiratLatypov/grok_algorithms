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
