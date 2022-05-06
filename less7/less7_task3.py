class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell


    def __add__(self, other):
        return Cell(self.count_cell+other.count_cell)

    def __sub__(self, other):
        return Cell(self.count_cell - other.count_cell)

    def __mul__(self, other):
        return Cell(self.count_cell * other.count_cell)

    def __truediv__(self, other):
        return Cell(float(f'{self.count_cell / other.count_cell:.00f}'))

    def make_order(self, count_cell_row):
        if self.count_cell<2:
            return 'Количество клеток меньше 2'

        str_result =''
        temp_i=1
        for i in range(count_cell_row+1, self.count_cell+2,count_cell_row):
            str_result+=str_result.join('\n')+'\t'.join('*' for num in range(temp_i,i))

            #print(str(num) for num in range(temp_i,i))
            #str_result.join('/n'+str(range(temp_i,i)))
            temp_i = i
        str_result += str_result.join('\n') + '\t'.join('*' for num in range(self.count_cell% count_cell_row))
        return str_result

    def __str__(self):
        return f'{self.count_cell}'


cell_1 = Cell(55)
cell_2 = Cell(60)

cell_sum = cell_1+cell_2
print(cell_sum)
print(cell_sum.make_order(7))

cell_sum = cell_1-cell_2
print(cell_sum)
print(cell_sum.make_order(7))

cell_sum = cell_1*cell_2
print(cell_sum)
print(cell_sum.make_order(20))

cell_sum = cell_1/cell_2
print(cell_sum)
print(cell_sum.make_order(20))