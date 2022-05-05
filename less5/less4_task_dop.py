import json

def return_tov_list(f_txt, tov_list,struct_list):
    for line in f_txt:
        if 'Товар' in line:
            yield dict(zip(struct_list,tov_list))
        else:
            tov_list.append(line.replace('\n',''))



struct_list = ['код','Удален','Наименование','КодГруппы','НаименованиеГруппа','Марка','Префикс','Артикул','Суффикс','Завод',
               'ТрНорма','Вес','ПолноеНаименование','Единица','Производитель','ГруппаЛим','КаталогНомер','Отдел',
               'НоменклатуранаяГРуппа','ЛиквидностьАВС','ЛиквидностьXYZ','Производитель1','ПроизводствоТД','ТипЦены','Наценка','Цена',]
json_list=[]
with open('tov.txt','r+') as f_txt:
    tov_list = []
    for item in return_tov_list(f_txt,tov_list,struct_list):
        json_list.append(item)
        tov_list.clear()
with open('tov.json','w+',encoding='utf-8') as tov_json:
    json.dump(json_list,tov_json,ensure_ascii=False, indent=4)

