from fractions import Fraction
import copy

class Matrix:
    def __init__(self, rows=0, cols=0, values=[]):
        self.data = values
        self.rows = rows
        self.cols = cols

    def read_from_stdin(self):
        self.data = []
        self.rows = int(input("Enter the number of rows: "))
        self.cols = int(input("Enter the number of cols: "))

        values = list(map(int, input("Enter the values separated by space: ").split()))

        index = 0
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(values[index])
                index += 1
            self.data.append(row)



    def add(self, m2):
        result_values = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + m2.data[i][j])
            result_values.append(row)

        return Matrix(self.rows, self.cols, result_values)

    def substraction(self, m2):
        result_values = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] - m2.data[i][j])
            result_values.append(row)
            
        return Matrix(self.rows, self.cols, result_values)

    def multiply(self, m2):
        if self.cols != m2.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")

        result_values = []
        for i in range(self.rows):
            row = []
            for j in range(m2.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * m2.data[k][j]
                row.append(total)
            result_values.append(row)
            
        return Matrix(self.rows, m2.cols, result_values)
    

    def determinant(self, *, use_fraction=False, eps=1e-12, copy_matrix=True):
    
        if self.rows == 0 and self.cols == 0:
            return 1  

        if self.rows != self.cols:
            raise ValueError("The matrix must be square (n x n) to calculate its determinant.")

        n = self.rows

        B = copy.deepcopy(self.data) if copy_matrix else self.data

        if use_fraction:
            for i in range(n):
                for j in range(n):
                    B[i][j] = Fraction(B[i][j])
            zero_test = lambda x: x == 0
            abs_val = lambda x: abs(x)
        else:
            for i in range(n):
                for j in range(n):
                    B[i][j] = float(B[i][j])
            zero_test = lambda x: abs(x) < eps
            abs_val = lambda x: abs(x)

        swaps = 0

        for k in range(n):
            p = max(range(k, n), key=lambda r: abs_val(B[r][k]))

            if zero_test(B[p][k]):
                return Fraction(0) if use_fraction else 0.0

            if p != k:
                B[k], B[p] = B[p], B[k]
                swaps += 1

            pivot = B[k][k]
            for i in range(k + 1, n):
                factor = B[i][k] / pivot
                for j in range(k, n):
                    B[i][j] -= factor * B[k][j]
                B[i][k] = 0 if not use_fraction else Fraction(0)

        prod = Fraction(1) if use_fraction else 1.0
        for i in range(n):
            prod *= B[i][i]

        if swaps % 2 == 1:
            prod = -prod

        return prod