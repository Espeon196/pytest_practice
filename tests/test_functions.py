from src.foo.functions import f, f_list


def test_f():
    """f()の戻り値を検証する"""
    assert f() == 3


def test_f_list():
    n = 3
    assert len(f_list(n)) == n, 'n個の要素が含まれていない'
