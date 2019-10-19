# Write a decorator arg_rules that validates arguments passed to the function
# A decorator should take 3 arguments:
#   max_length: 15
#   type_: str
#   contains: []  - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed
#
# Otherwise return result
from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            cont = bool
            reasons = f'{func.__name__} failed for these reasons: '
            arg_string = "".join(map(str, args))
            for el in contains:
                if el not in arg_string:
                    cont = False
                    print(f'{reasons} because of contains')
                    return False
            if len(arg_string) > max_length:
                print(f'{reasons} because of length')
                return False
            if len(arg_string) < max_length and cont:
                return func(arg_string)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('S@SH05'))
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
