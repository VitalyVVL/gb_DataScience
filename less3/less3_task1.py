def my_division(x,y):
  """Функция деления
  Выходные парамерты:
  х - число
  y - число
  Возвращаемое занчение:
  Результат деления
  """
  try:
        return x/y
  except:
        print("Деление на ноль не возможно")
        return 0


x = int(input("Введите числитель: "))
y = int(input("Введите знаменатель: "))
print(f"Результат деления: {my_division(x,y):.2f}")