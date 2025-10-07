
def multiply(data, scalar):
    result = []
    for i in range(len(data)):
        row = []
        for j in range(len(data[0])):
            row.append(data[i][j] * scalar)
        result.append(row)

    return result
