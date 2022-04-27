def fact_gen(user_num):
    f_num = 1
    for i in range(1,user_num+1):
        f_num*=i
        yield f_num


for el in fact_gen(int(input("Введите число для расчета фактариала: "))):
    print(el)