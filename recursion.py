def countdown(i):
    print(i)
    if i <= 1:
        # базовый случай
        return
    countdown(i - 1)
