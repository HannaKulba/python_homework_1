import time
import requests


def execution_time(func):
    def wrapper(url):
        start_time = time.time()
        content = func(url)
        end_time = time.time()
        exec_time = end_time - start_time
        print('Время выполнения функции "' + func.__name__ + '" составляет ' + str(exec_time) + ' секунд.')
        return content

    return wrapper


@execution_time
def get_webpage_content(url):
    webpage = requests.get(url)
    return webpage.text


if __name__ == '__main__':
    print(get_webpage_content('https://senlainc.com/'))
