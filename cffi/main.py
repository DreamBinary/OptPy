# -*- coding:utf-8 -*-
# @FileName : main.py
# @Time : 2024/2/17 17:57
# @Author : fiv

import test_py
import test_cffi
from time_test import time_test


@time_test
def main_py(n):
    print(test_py.test(n))


@time_test
def main_cffi(n):
    print(test_cffi.test_cffi(n))


if __name__ == '__main__':
    main_py(1000000)
    main_cffi(1000000)
