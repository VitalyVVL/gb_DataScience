
rating = [7,5,3,3,2]
for temp_i in range(3):
    print("Текущее состояние рейтинга: ",rating)
    i = int(input("Введите число для включения в рейтинг: "))
    flag = False
    for j in range(len(rating)):
        if rating[j]<i:
            rating.insert(j,i)
            flag = True
            break
    if not flag:
        rating.append(i)
print('Итоговое состояние рейтинга: ',*rating)