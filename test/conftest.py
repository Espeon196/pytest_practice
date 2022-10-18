import pytest
import smtplib
from .test_foocompare import Foo


@pytest.fixture
def assert_list_match():
    """check whether two lists have the same components"""

    def _assert_list_match(list1, list2):
        assert sorted(list1) == sorted(list2)
    return _assert_list_match


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return [
            "Comparing Foo instances:",
            f"  vals: {left.val} != {right.val}",
        ]


@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
