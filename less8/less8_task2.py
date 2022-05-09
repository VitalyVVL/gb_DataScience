class My_Error(Exception):
 pass
 #def __str__(self):
  #   return f'деление на 0'

a = input("Введите a: ")
b = input("Введите b: ")

try:
    a = int(a)

except ValueError:
    print(('А - не явялется числом'))

try:
    b = int(b)
    if b==0:
        raise My_Error('B - не может быть ранвно  0')

except ValueError:
    print(('B - не явялется числом'))

except My_Error as err:
    print(err)
else:
    print(f'a/b = {a / b}')

