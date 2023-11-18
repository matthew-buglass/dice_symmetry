from functools import wraps
from time import time_ns


def timed(func):
    """
    A decorator to time a function
    :param func: The decorated function
    :return: (result, execution time in ms)
    """
    @wraps(func)
    def timed_wrapper(*args, **kwargs):
        t1 = time_ns()
        res = func(*args, **kwargs)
        t2 = time_ns()
        ex_time = (t2 - t1) / 1000000
        return res, ex_time
    return timed_wrapper