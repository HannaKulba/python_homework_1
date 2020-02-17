def bucket(*args, **kwargs):
    def wrapper(func):
        result = (args, kwargs)
        print(result)
        return func

    return wrapper


@bucket(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
# @bucket()
def identity(x):
    return x


if __name__ == '__main__':
    print(identity(42))
