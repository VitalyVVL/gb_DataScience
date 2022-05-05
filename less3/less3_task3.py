def my_fun(*args):
    args = list(args)
    x= max(args)
    args.remove(max(args))
    y = max(args)
    return x,y,x*y


a= int(input("Введите аргумент 1: "))
b= int(input("Введите аргумент 2: "))
c= int(input("Введите аргумент 3: "))

res = my_fun(a,b,c)
print(f"Произведение максиальных числе {res[0]} и {res[1]} равно {res[2]}")