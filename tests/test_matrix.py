from matrix import Matrix
from fractions import Fraction
import pytest

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


def test_matrix_multiply():
    m1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    m2 = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])
    
    r = m1.multiply(m2)
    
    assert r.rows == m1.rows
    assert r.cols == m2.cols
    assert r.data == [[58, 64], [139, 154]]


def test_matrix_determinant():
    m1 = Matrix(3, 3, [[1, 2, 3], [0, 1, 4], [5, 6, 0]]) 
    assert m1.determinant(use_fraction=False) == pytest.approx(1.0)
    assert m1.determinant(use_fraction=True) == Fraction(1)

def test_matrix_transpose():
    m1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
    
    r = m1.transpose()
    
    assert r.rows == m1.cols
    assert r.cols == m1.rows
    assert r.data == [[1, 4], [2, 5], [3, 6]]

def test_matrix_inverse():
    m1 = Matrix(2, 2, [[1,2],[3,4]])

    r = m1.inverse()

    assert r.data == [[-2.0,1.0],[1.5,-0.5]]

