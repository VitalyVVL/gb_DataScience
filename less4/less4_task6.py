from itertools import cycle, count

my_list = []
for i in count(int(input('Введите стартовое число: '))):
    print(i, end='')
    my_list.append(i)
    quit = input()
    my_list.append(quit)
    if quit=='q':
        break

my_list2 = []
my_cycle = cycle(my_list)
for _ in range(1, len(my_list)):
    a = next(my_cycle)
    if a in my_list2:
        break
    else: my_list2.append(a)
print(my_list2)
