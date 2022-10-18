from src.foo import lists


def test_foo_lists(assert_list_match):
    l1, l2 = lists.foo_lists()
    assert_list_match(l1, l2)
