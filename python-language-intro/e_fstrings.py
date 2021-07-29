"""
Format Strings

https://www.python.org/dev/peps/pep-0498/
"""


def main():
    print('OG string format: %s' % ('hello!',))

    print('{}{}{}'.format('improved format', 'asdf', 'zxcv'))
    print('{first}, {second}'.format(second='improved format with named args', first='i am the first argument'))

    fstrings = ''
    print(f'{fstrings}')

    # you can also run code inside the brackets
    print(f'{2 + 7}')
    print(f'{", ".join([str(i) for i in range(10)])}')


if __name__ == '__main__':
    main()
