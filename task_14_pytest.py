from task_14_matrix import Matrix
import pytest

m1 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
m2 = Matrix(([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def test_add_matrix():
    assert m1 + m2 == Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]]))


def test_equal_matrix():
    assert m1 == m2


def test_not_equal_matrix():
    assert m1 != Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]]))


def test_greater_matrix():
    assert Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]])) > m2


def test_less_matrix():
    assert m1 < Matrix(([[2, 4, 6], [8, 10, 12], [14, 16, 18]]))


if __name__ == '__main__':
    pytest.main(['-vv'])
