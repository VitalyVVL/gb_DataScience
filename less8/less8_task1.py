class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        try:
            return f'Вы ввели {self.day} {Date.get_month()[self.month-1]} {self.year}'
        except:
            return "None"

    @classmethod
    def set_date(cls, date):
        date_list = date.split('-')
        if len(date_list)<3:
             print(f'Неоходимо введсти даты в формате dd-mm-yyyy, сейчас формат не соответтвует')
             return None

        return Date(Date.validete_date(date_list[0], 'day'), Date.validete_date(date_list[1], 'month'),
                    Date.validete_date(date_list[2], 'year'))

    @staticmethod
    def validete_date(user_date, flag):
        try:
            user_date = int(user_date)
        except ValueError:
            print(f'Неоходимо введсти даты в формате dd-mm-yyyy, сейчас формат не соответтвует {user_date}')
            return None

        if flag == 'day':
            if not(1<=user_date<=31):
                print(f'Дни должны быть в диапазоне между 1-31 вы указали {user_date}')
                return None
        elif flag == 'month':
            if not(1<=user_date<=12):
                print(f'Месяц должн быть в диапазоне между 1-12 вы указали {user_date}')
        elif flag == 'year':
            if not(1000<=user_date<=3000):
                print(f'Год должн быть 4-х значным числом {user_date}')

        return user_date

    @staticmethod
    def get_month():
         return ['январь','февраль','март','авпрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декбрь']


date_1 = Date.set_date(input("Введите дату в формате dd-mm-yyyy: "))
print(date_1)