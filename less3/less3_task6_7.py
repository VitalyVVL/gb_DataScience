def my_func(word):
    return word[0].upper()+word[1:].lower()

user_string = input("Введите строку: ").split()
for i,word in enumerate(user_string):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('Введите строку без заклавных букв')
    else:
        user_string[i] = my_func(word)

print(' '.join(user_string))
