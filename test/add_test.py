import sys

import pytest

from add import add


def test_add():
    assert add(1, 2) == 3


@pytest.mark.slow
def test_add_large():
    assert add(10, 20) == 30


if __name__ == "__main__":
    pytest.main(sys.argv)
