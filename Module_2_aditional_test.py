def get_password(n):
    result = ""

    for i in range(1, n):  # числа от 1 до n-1
        for j in range(i + 1, n + 1):  # числа от i+1 до n
            if (i + j) % n == 0:
                result += f"{i}{j}"  # Добавляем пару в результат в виде строки "xy"

    return result


print(get_password(int(input("Введите первое число (от 3 до 20): "))))
