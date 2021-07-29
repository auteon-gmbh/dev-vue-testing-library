"""
Comprehensions

https://www.python.org/dev/peps/pep-0202/
https://www.python.org/dev/peps/pep-0274/
"""


def simple_squares():
    squares = []
    for x in range(10):
        squares.append(x ** 2)

    return squares


def fp_squares():
    return list(map(lambda x: x ** 2, range(1000)))


def list_comp_squares():
    return [x * x for x in range(1000)]


responses = [{'id': '123', 'a': 5},
             {'id': '932', 'a': 926},
             {'id': '9145', 'a': 100}]


response_by_id = {resp.get('id'): resp for resp in responses}
