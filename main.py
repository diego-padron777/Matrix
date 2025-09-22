#Hacer una clase que lea 2 matrices bidimensionales (enter rows and columns) y que ingrese los valores(enter values)
#

#Luego hacer la suma de las 2 matrices y mostrar el resultado

class Matrix:
    def __init__(self, rows, cols, values):
        self.rows = rows
        self.cols = cols

        self.data = []
        index = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(values[index])
                index += 1
            self.data.append(row)


rows = int(input('Enter the number of rows: '))
cols = int(input('Enter the number of cols: '))

values1 = list(map(int, input('Enter the values separated by space: ').split()))
matrix1 = Matrix(rows, cols, values1)
values2 = list(map(int, input('Enter the values separated by space: ').split()))
matrix2 = Matrix(rows, cols, values2)


def add_matrices(m1, m2):

    result_values = []
    for i in range(m1.rows):
        for j in range(m1.cols):
            result_values.append(m1.data[i][j] + m2.data[i][j])

    return Matrix(m1.rows, m1.cols, result_values)

result_matrix = add_matrices(matrix1, matrix2)
print("Resultant Matrix:")
for row in result_matrix.data:
    print(row)

    


