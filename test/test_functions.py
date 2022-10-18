from src.foo.functions import f, f_list, f_value_error
import pytest


def test_f():
    """f()の戻り値を検証する"""
    assert f() == 3


def test_f_list():
    n = 3
    assert len(f_list(n)) == n, 'n個の要素が含まれていない'


def test_f_value_error():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        f_value_error()
