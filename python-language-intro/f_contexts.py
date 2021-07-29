"""
Context Managers

https://www.python.org/dev/peps/pep-0343/
"""


def read_file():
    with open('zasdf.txt') as f:
        for line in f:
            print(line.strip())


class Something:
    def __init__(self):
        pass

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


if __name__ == '__main__':
    # read_file()

    with Something() as s:
        print('doing something there')
