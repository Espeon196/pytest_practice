from src.foo import sysexit
import pytest


def test_mytest():
    with pytest.raises(SystemExit):
        sysexit.f()
