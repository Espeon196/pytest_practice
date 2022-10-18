from src.foo import letters


def contains_all_letters(subject_string, letters):
    """check whether string contains all letters"""
    return all(li in subject_string for li in letters)


def test_foo():
    assert contains_all_letters(letters.foo_letters(), 'aA1')
