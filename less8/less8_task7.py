class ComplexNum:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        x1, y1 = ComplexNum.parse(self.num)
        x2, y2 = ComplexNum.parse(other.num)

        real_part = x1 + x2
        imaginary_part =  y2 * y1
        result =str(real_part) + '+' + str(imaginary_part) + 'i' if imaginary_part >= 0 else str(real_part) + str(imaginary_part) + 'i'
        return ComplexNum(result)

    def __mul__(self, other):
        x1, y1 = ComplexNum.parse(self.num)
        x2, y2 = ComplexNum.parse(other.num)

        real_part = x1 * x2 - y1 * y2
        imaginary_part = x1 * y2 + x2 * y1
        result = str(real_part) + '-' + str(imaginary_part) + 'i' if imaginary_part >= 0 else str(real_part) + str(imaginary_part) + 'i'
        print(result)
        #return ComplexNum(result)

    def __str__(self):
        return f'{self.num}'

    @staticmethod
    def parse(num):
        num = num[:-1]
        if '+' in num:
            num_list = num.split('+')
        else:
            num_list = num.split('-')
            if num_list[0] == '-':
                num_list.pop(num_list[0])
                num_list[0] = '-' + num_list[0]

            num_list[1] = - int(num_list[1])
        return tuple(map(int, num_list))


number_1 = ComplexNum('5 + 4i')
number_2 = ComplexNum('3 - 2i')

num_sum = number_1 + number_2
num_mul = number_1 * number_2

print(num_sum)
# print(num_mul)
