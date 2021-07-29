"""
Decorators

https://www.python.org/dev/peps/pep-0318/
https://docs.python.org/3/library/functools.html

Good explanations:
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html#decorators-with-arguments
"""

from functools import wraps


def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} called with args:{args}')
        return func(*args, **kwargs)

    return wrapper


def call_count(func):
    @wraps(func)
    def function_wrapper(*args, **kwargs):
        function_wrapper.calls += 1
        print(f'{func.__name__} called {function_wrapper.calls} times')
        return func(*args, **kwargs)

    function_wrapper.calls = 0

    return function_wrapper


def call_count_with_args(*decorator_args, **decorator_kwargs):
    def decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            function_wrapper.calls += 1
            if not decorator_kwargs.get('skip', False):
                print(f'{func.__name__} called {function_wrapper.calls} times')
            return func(*args, **kwargs)

        function_wrapper.calls = 0

        return function_wrapper

    return decorator


@call_count
def print_hello():
    print('hello')


@call_count_with_args('test', skip=True)
def add(*args):
    return sum(args)


if __name__ == '__main__':
    add(1, 2, 3, 4)
    add(1, 2, 3, 4)
    add(1, 2, 3, 4)
    add(1, 2, 3, 4)
