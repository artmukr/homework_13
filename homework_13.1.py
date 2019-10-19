# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#   "add called with 4, 5"
from functools import wraps


def logger(func):
    @wraps(func)
    def decorator(*args):
        a = ', '.join(map(str, args))
        return f"{func.__name__} called with {a}"
    return decorator


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(square_all(4, 4))
print(add(5, 5))
