def memoized(maxsize=0):
    def actual_decorator(func):
        memory = {}

        def wrapper(*args):
            memoization_key = str(args[0]) + ' ' + str(args[1])
            result = func(*args)
            if memoization_key not in memory:
                if len(memory) >= maxsize:
                    lastKey = list(memory.keys())[len(memory) - 1]
                    memory.pop(lastKey)
                memory.update({memoization_key: result})
            else:
                memory[memoization_key] = result
            return memory[memoization_key]

        return wrapper

    return actual_decorator


@memoized(maxsize=2)
def sum_of_two(a, b):
    print(a, b, end='; ')
    return a + b


if __name__ == '__main__':
    print(sum_of_two(2, 0), '\n')
    print(sum_of_two(2, 0), '\n')

    print(sum_of_two(4, 2), '\n')
    print(sum_of_two(4, 2), '\n')

    print(sum_of_two(5, 0), '\n')
    print(sum_of_two(5, 0), '\n')

    print(sum_of_two(4, 2))
