"""
Typing

https://docs.python.org/3/library/typing.html

Use mypy or similar
"""

from typing import Union


def test() -> str:
    return 'test'


def add(*args: Union[int, float]) -> float:
    return sum(args)


if __name__ == '__main__':
    test()
