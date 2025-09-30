from matrix import Matrix

matrix1 = Matrix()
matrix1.read_from_stdin()



result = matrix1.inverse()

print("Resultant Matrix:")
for row in result.data:
    print(row)
