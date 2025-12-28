from __future__ import annotations

from src.main import divide
from src.main import reverse_string


def test_divide():
    assert divide(2, 1) == 2
    assert divide(3, 3) == 1


def test_reverse_string(number_list):
    assert reverse_string(number_list) == [5, 4, 3, 2, 1]
