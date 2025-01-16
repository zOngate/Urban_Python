my_dict = {"Peter": 1986, "Jonathan": 1868, "Joseph": 1920}
print("Словарь:",my_dict)
print("Существующее значение :",my_dict["Peter"])
print("Не существующее значение :",my_dict.get("Dio"))
my_dict.update({"Abdul": 1960,"Polbareff": 1964})
print("Удалённое значение :",my_dict.pop("Peter"))
print("Изменённый словарь :", my_dict)

print("--------------------------------")

my_set = {1,5,4,2,5,7,1,2,7,4,1,5,8,4,1,5, "sstraa", 4.25}
print("Множество :", my_set)
my_set.update([9999999999999, "OVER 9000"])
my_set.discard(7)
print("Изменённый множество :",my_set)