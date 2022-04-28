import os.path as path
if path.isfile('my_fyle.txt'):
    f_obj = open('my_file.txt', 'a+', encoding='utf-8')
else:
    f_obj = open('my_file.txt', 'w+', encoding='utf-8')
while True:
    my_line = input("Введите данные для файла: ")
    if my_line=='':
        break
    f_obj.writelines(my_line+'\n')

print('=======Содержимое файла==========')
f_obj.seek(0)
for line in f_obj:
    print(line, end='')

f_obj.close()