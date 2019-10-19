# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


def stop_words(words: list):
    def decorator(func):
        def wrapper(*args):
            a = func("".join(map(str, args)))
            # a = [a.replace(word, "*") for word in words]
            for word in words:
                a = a.replace(word, "*")
            return a
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# print(create_slogan("Steve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
