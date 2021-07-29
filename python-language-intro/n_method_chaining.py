"""
Method Chaining
"""

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, by=None):
        if by is not None:
            self.count += by
        else:
            self.count += 1

        return self

    def decrement(self, by=None):
        if by is not None:
            self.count -= by
        else:
            self.count -= 1

        return self


def main():
    c1 = Counter().increment(by=10).decrement()
    print(c1.count)


if __name__ == '__main__':
    main()
