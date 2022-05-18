with open('temp_num.txt', 'w+') as f:
    for i in range(1, int(input("Введите число для расчета: ")) + 1):
        f.write(f'{i} ')
    f.seek(0)
    list_user = list(map(int, f.read().split()))
    print(list_user)
    print(sum(list_user))
