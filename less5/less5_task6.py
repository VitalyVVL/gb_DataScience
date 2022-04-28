
with open('re_edu.txt','r',encoding='utf-8') as f:
    for line in f:
        temp_line = line.replace('(',' ')
        print({line.split(':')[0]:sum([int(s) for s in temp_line.split() if s.isdigit()])})
