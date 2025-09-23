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

def add_matrices(m1, m2):

    result_values = []
    for i in range(m1.rows):
        for j in range(m1.cols):
            result_values.append(m1.data[i][j] + m2.data[i][j])

    return Matrix(m1.rows, m1.cols, result_values)
