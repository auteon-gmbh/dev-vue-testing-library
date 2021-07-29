"""
Generators - The lazy iterator

https://www.python.org/dev/peps/pep-0255/
https://www.python.org/dev/peps/pep-0289/
"""


def even_num_gen():
    num = 0
    while True:
        yield num
        num += 2


def main():
    evens = even_num_gen()

    print(next(evens))
    print(next(evens))
    print(next(evens))

    print([next(evens) for i in range(100)])


if __name__ == '__main__':
    main()
