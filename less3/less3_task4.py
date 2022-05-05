def my_func(x,y):
    reslt1 = x**y
    reslt2 = x
    for i in range(abs(y)-1):
     reslt2*=x
    if y<0:
     reslt2 = 1/reslt2

    return reslt1,reslt2


x = float(input("Введите аргумент: "))
y = int(input("Введите степень: "))
result = my_func(x,y)
print(f"Варинат1 : {result[0]} варинат2: {result[1]}")