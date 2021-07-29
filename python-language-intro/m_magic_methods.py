"""
Magic methods

Best reference that I've found:

https://rszalski.github.io/magicmethods/
"""


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, by=None):
        if by is not None:
            self.count += by
        else:
            self.count += 1

    def __str__(self):
        return str(self.count)

    def __repr__(self):
        return f'{self.__class__.__name__} count: {self.count}'

    def __eq__(self, other):
        if isinstance(other, Counter):
            return self.count == other.count

    def __ne__(self, other):
        if isinstance(other, Counter):
            return self.count != other.count

    def __gt__(self, other):
        if isinstance(other, Counter):
            return self.count > other.count

    def __lt__(self, other):
        if isinstance(other, Counter):
            return self.count < other.count


def main():
    c1 = Counter()
    c1.increment(by=10)
    c2 = Counter()
    c2.increment(by=10)

    print(c1 == c2)
    print(c1 != c2)
    print(c1 > c2)
    print(c1 < c2)

    print(str(c1))
    print(repr(c1))


if __name__ == '__main__':
    main()
