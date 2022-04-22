goods = []
good = {}
reg_goods_dict = {'name':'Наименование','price':'Цена','quantity':'Количество', 'unit':'единица измерения'}
num_goods = int(input("Введите количество новых позиций: "))
for _ in range(num_goods):
 good = reg_goods_dict.copy()
 for name_reg in reg_goods_dict:
    good[name_reg] =input(f"Введите {reg_goods_dict[name_reg]}: ")
 goods.append(good)
print(goods)

goods_diсt = reg_goods_dict.copy()
for good_dict in goods_diсt:
    goods_diсt[good_dict] = []

for good in goods:
    for name_reg in reg_goods_dict:
        if good[name_reg] not in goods_diсt[name_reg]: goods_diсt[name_reg].append(good[name_reg])
print(goods_diсt)