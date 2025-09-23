class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.data = [[]]

    def read(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of cols: "))

        values = list(map(int, input("Enter the values separated by space: ").split()))

        index = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(values[index])
                index += 1
            self.data.append(row)



    def add(self, m2):
        result_values = []
        for i in range(self.rows):
            for j in range(self.cols):
                result_values.append(self.data[i][j] + m2.data[i][j])

        return Matrix(self.rows, self.cols, result_values)
