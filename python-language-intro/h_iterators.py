"""
Iterators

https://www.python.org/dev/peps/pep-0234/
"""
import random


class NumIter:
    def __init__(self, nums):
        self.cur = 0
        self.iter_len = nums

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur == self.iter_len:
            raise StopIteration

        elif self.cur < self.iter_len:
            self.cur += 1
            return self.cur
        else:
            raise StopIteration


def main():
    a_str = 'this is an iterator'
    a_list = ['this', 'is', 'also', 'an', 'iterator']

    # also an iterator
    a_dict = {''.join(chr(random.randrange(65, 90)) for i in range(5)): random.random() for i in range(20)}

    # for k in a_dict:
    #     print(k, a_dict[k])

    num_iter = NumIter(10)

    for i in num_iter:
        print(i)


if __name__ == '__main__':
    main()
