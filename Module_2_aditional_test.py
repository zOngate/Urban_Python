def get_password(n):
    result = ""

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                result += f"{i}{j}"

    return result


print(get_password(int(input("Введите первое число (от 3 до 20): "))))
