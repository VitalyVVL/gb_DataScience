with open('my_fyle.txt','r') as f:
    for i,line in enumerate(f):
        print(f'Количество слов в строке № {i} : {len(line.split())}')

    f.seek(0)
    text = f.read()
    count_line = text.count('\n')
    print(f'Количество строк: {count_line}')
