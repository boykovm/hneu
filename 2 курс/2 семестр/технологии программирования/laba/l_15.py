from datetime import datetime


def logger(method):
    def wrapper(ref, *args, **kwargs):
        logs = open('logs.log', 'a+')
        logs.write(f'function {method.__name__} starts at {datetime.now().isoformat()}\n')
        result = method(ref, *args, **kwargs)
        logs.write(f'function {method.__name__} ends at {datetime.now().isoformat()} with result {result}\n')
        logs.close()
        return result
    return wrapper

class SquareQueue:
    def __init__(self, length: int = 0):
        self.__length = length
        self.__generate_queue()


    @logger
    def __generate_queue(self):
        self.__square_queue = [x * x for x in range(self.__length)]

    @logger
    def sum_of_elements(self, count: int = 10):
        return sum(self.__square_queue[:count])

    @logger
    def __str__(self):
        return ', '.join(map(str, q.__square_queue))

if __name__ == '__main__':
    q = SquareQueue(9)
    print(q.sum_of_elements())
    print(q.sum_of_elements(100))
    print(q.sum_of_elements(1000))
    print(q)
