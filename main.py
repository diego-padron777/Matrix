from matrix import Matrix, add_matrices

matrix1 = Matrix()
matrix1.read_from_stdin()

matrix2 = Matrix()
matrix2.read_from_stdin()


result = matrix1.add(matrix2)

print("Resultant Matrix:")
for row in result.data:
    print(row)
