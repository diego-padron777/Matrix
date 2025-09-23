from matrix import Matrix, add_matrices

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

values1 = list(map(int, input("Enter the values separated by space: ").split()))
matrix1 = Matrix(rows, cols, values1)
values2 = list(map(int, input("Enter the values separated by space: ").split()))
matrix2 = Matrix(rows, cols, values2)


result_matrix = add_matrices(matrix1, matrix2)
print("Resultant Matrix:")
for row in result_matrix.data:
    print(row)
