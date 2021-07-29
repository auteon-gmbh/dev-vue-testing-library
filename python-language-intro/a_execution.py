"""
Code Execution

To prevent side effects, scripts should always implement the __name__ == '__main__' block
"""

print(f'imported {__name__}')


def add(a, b):
    print(f'add({a}, {b}): {a + b}')


def multiply(a, b):
    print(f'multiply({a}, {b}): {a * b}')


# only will be called on execution
if __name__ == '__main__':
    print('call  __name__ == \'__main__\'')
    multiply(2, 2)

# always executed, imported or runnable
add(1, 2)
