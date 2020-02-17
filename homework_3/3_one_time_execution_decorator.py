def one_time_execution(func):
    def wrapper(*args, **kwargs):
        try:
            return wrapper._once_result
        except AttributeError:
            wrapper._once_result = func(*args, **kwargs)
            return wrapper._once_result

    return wrapper


@one_time_execution
def identity(x):
    return x


if __name__ == '__main__':
    print(identity(73))
    print(identity(42))
