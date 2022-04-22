
str_user = input("Введите строку: ").split()
for i,word in enumerate(str_user,1):
    print(f"{i}: {word[:10]}")