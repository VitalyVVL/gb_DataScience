

class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result = ''
        for line in self.matrix_list:
            result += result.join('\n')+'\t'.join(str(n) for n in line)
        return result

    def __add__(self, other):
      result_list = []

      for i in range(min(len(self.matrix_list), len(other.matrix_list))):
          line_list = []
          for j in range(min(len(self.matrix_list[i]),len(other.matrix_list[i]))):
              line_list.append((self.matrix_list[i][j]+other.matrix_list[i][j]))

          result_list.append(line_list)
      return Matrix(result_list)
            #Matrix(map(sum, zip(self.matrix_list, other.matrix_list)))

matrix_1 = Matrix([[31,22],[37,43],[51,86]])
matrix_2 = Matrix([[3,5,32],[2,4,6],[-1,64,-8]])
matrix_3 = Matrix([[3,5,8,3],[8,3,7,1]])

print(matrix_1)
matrix_sum = matrix_1+matrix_2+matrix_3
print(matrix_sum)