from statistics import mean
work_dict = {'soname':'','name':'','salary':''}
work_list = ['soname','name','salary']
salary_list =[]
with open('wages_of_workers.txt','r', encoding='utf-8') as f:
     for i,line in enumerate(f):
        work_dict = dict(zip(work_dict, line.split()))
        try:
            salary_list.append(float(work_dict['salary']))
            if float(work_dict['salary'])<20000:

                print(work_dict)
        except ValueError:
            print(f"Невозможно приобразовать число {work_dict['salary']}")
     print(f'Средная заработная плата для  {len(salary_list)} = {mean(salary_list)} общая сумма {sum(salary_list)}')