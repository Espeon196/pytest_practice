
class Foo:
    def __init__(self, val: int):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    f1 = Foo(2)
    f2 = Foo(1)
    assert f1 == f2
