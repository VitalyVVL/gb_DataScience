def my_fun(struct_user):
    print(struct_user)


str_user = {"имя":"", "фамилия":"", "год рождения":"", "город проживания":"", "email":"", "телефон":""}
for item in str_user:
    str_user[item] = input("Введите "+item+" :")

my_fun(str_user)