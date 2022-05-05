def my_fync_gen(my_list, repeated_list, uniqui_list):
    for i, element in enumerate(my_list):
        if element in repeated_list:
            continue
        if element in uniqui_list:
            repeated_list.append(element)
            uniqui_list.remove(element)
        else:
            uniqui_list.append(element)
        yield repeated_list, uniqui_list


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
repeated_list = []
uniqui_list = []
my_gen = my_fync_gen(my_list, repeated_list,uniqui_list)
for i in range(1, len(my_list)-1):
   repeated_list, uniqui_list = next(my_gen)
   print(f"========Итерация {i}================")
   print(f"Не уникальный список: {repeated_list}")
   print(f"Уникальный список : {uniqui_list}")





