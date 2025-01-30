numbers_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

answ_len = 0

while answ_len < len(numbers_list):
    if numbers_list[answ_len] < 0:
        break
    if numbers_list[answ_len] > 0:
        print(numbers_list[answ_len])
    answ_len += 1
