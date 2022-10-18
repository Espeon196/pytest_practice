from typing import List


def f():
    """
    常に定数3を返す関数

    Returns:
        int: 3
    """
    return 3


def f_list(n: int) -> List[int]:
    """
    nより小さい非負整数を昇順に並べたリストを返す関数(の間違い)

    Args:
        n (int): 必要なリストの要素数

    Returns:
        List[int]: nより小さい非負整数を昇順に並べたリスト
    """
    return [i for i in range(n)]


def f_value_error():
    """常にエラーを返す関数

    Raises:
        ValueError: 数値エラー
    """
    raise ValueError("Exception 123 raised")
