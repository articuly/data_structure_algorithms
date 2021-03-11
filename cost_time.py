import time

__all__ = ['cost_time']


def cost_time(func):
    """Decorator of viewing function runtime.
    eg:
       from cost_time import cost_time as ct
       @ct
       def work(...):
           print('work is running')
       word()
       # work is running
       # <work> cost time: 2.8371810913085938e-05
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('{} cost time: {}'.format(func.__name__, end_time - start_time))
        return res

    return wrapper
