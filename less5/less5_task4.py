from translate import Translator as user_tr
tr = user_tr(to_lang="ru")
with open('num_en.txt','r',encoding='utf-8') as f_read:
    with open('num_ru.txt','w',encoding='utf-8') as f_write:
        for line in f_read:
            tr_ru = tr.translate(line)
            print(tr_ru)
            f_write.write(tr_ru+'\n')
            #print(result_translate.translate(to='en'))
                #= tr.translate('fist',src='auto',dest='ru')
            #print(result_translate.text,end='')
                          #tr.translate(line,'en', 'ru'))
