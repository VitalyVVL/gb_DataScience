def my_func(s,flag):
    in_list = input('Введите числа через проблел или Q для выхода: ').upper().split()
    for i in in_list:
        if i == "Q":
            flag = True
            break
        else:
            try:
                s+=float(i)
            except ValueError: print(f'Заначние {i} не возожно сложить ')
    return s,flag


s=0
flag = False
while True:
    s,flag = my_func(s,flag)
    if flag:
      print(f"Итоговый результат: {s:.2f}")
      break
    else:
        print(f"Промежуточный результат: {s:.2f}")