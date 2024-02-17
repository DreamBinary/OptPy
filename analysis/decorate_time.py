# -*- coding:utf-8 -*-
# @FileName : decorate_time.py
# @Time : 2024/2/17 19:46
# @Author : fiv
import time


def timefn(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"function {fn.__name__} took {end - start} seconds")
        return result

    return wrapper
