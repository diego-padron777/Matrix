from matrix import Matrix

def test_matrix_substraction():
    m1 = Matrix(2,2,[[1,1],[1,1]])
    m2 = Matrix(2,2,[[2,2],[2,2]])

    r = m1.substraction(m2)

    assert r.rows == m1.rows
    assert r.cols == m1.cols
    assert r.data == [[-1,-1],[-1,-1]]

def test_matrix_add():
    m1 = Matrix(2,2,[[1,1],[1,1]])
    m2 = Matrix(2,2,[[2,2],[2,2]])

    r = m1.add(m2)

    assert r.rows == m1.rows
    assert r.cols == m1.cols
    assert r.data == [[3,3],[3,3]]

def test_matrix_add_1x1():
    m1 = Matrix(1,1,[[2]])
    m2 = Matrix(1,1,[[1]])

    r = m1.add(m2)

    assert r.rows == m1.rows
    assert r.cols == m1.cols
    assert r.data == [[3]]
