def message(string: str) -> int:
    """
    Находит количество `quantity` различных комбинаций букв, которые
    при кодировании заданным методом дают строку `string`
    """
    f = [0] * (len(string) + 1)
    f[0] = 1
    f[1] = 1
    for i in range(2, len(string) + 1):
        f[i] = f[i - 1] + f[i - 2] * int(int(string[i - 2]) != 0 and int(string[i - 2: i]) <= 33)
    return f[-1]
