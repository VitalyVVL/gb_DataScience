from functools import reduce as red

print(red(lambda a,b: a * b,[num for num in range(100, 1001,2)]))