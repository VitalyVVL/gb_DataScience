class Exseptiom_Int(Exception):
    pass

my_list = []
while True:
    try:
      a = input('Введите целое число: ')
      if a =='stop':
          break
      elif not a.isdigit():
         raise Exseptiom_Int('Ошибка нужно введить только целые числа')
    except Exseptiom_Int as  err:
        print(err)
    else:
        my_list.append(a)

print(my_list)
