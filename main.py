from matrix import Matrix

A = Matrix()
A.read_from_stdin()

B = Matrix()
B.read_from_stdin()

#x = A/B = A * B^-1

B_inv = B.inverse()
result = A.multiply(B_inv)

print("Resultant Matrix:")
for row in result.data:
    print(row)
