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
            for j in range(self.cols):
                result_values.append(self.data[i][j] + m2.data[i][j])

        return Matrix(self.rows, self.cols, result_values)
