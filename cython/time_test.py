# -*- coding:utf-8 -*-
# @FileName : time_test.py
# @Time : 2024/2/13 14:34
# @Author : fiv


# a decorator to calculate the time of a function
def time_test(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time of {func.__name__} is {end - start}")
        return result

    return wrapper
