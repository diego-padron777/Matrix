from matrix import Matrix

class TestMatrixScalarMultiplication:
    def test_multiplication_by_scalar_1x1(self):
        # setup
        m1 = Matrix(1, 1, [[5]])
        scalar = 4

        # execute
        result = m1.multiply_by_scalar(scalar)

        # verify
        expected = Matrix(1, 1, [[20]])
        assert result.data == expected.data

    def test_multiplication_by_scalar(self):
        from matrix import Matrix

        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        scalar = 3
        result = m1.multiply_by_scalar(scalar)
        expected = Matrix(2, 2, [[3, 6], [9, 12]])
        assert result.data == expected.data
    
    def test_multiplication_by_scalar_negative(self):
        m1 = Matrix(2, 2, [[1, -2], [-3, 4]])
        scalar = -2
        result = m1.multiply_by_scalar(scalar)
        expected = Matrix(2, 2, [[-2, 4], [6, -8]])
        assert result.data == expected.data
    
    def test_multiplication_by_scalar_zero(self):
        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        scalar = 0
        result = m1.multiply_by_scalar(scalar)
        expected = Matrix(2, 2, [[0, 0], [0, 0]])
        assert result.data == expected.data
        