from sys import argv

def my_finc():
    print(argv)
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Оплата труда: {time*rate+bonus}')
    except ValueError:
        print("Введите 3 числа")

my_finc()