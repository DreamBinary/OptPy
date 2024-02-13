# -*- coding:utf-8 -*-
# @FileName : main.py
# @Time : 2024/2/13 14:28
# @Author : fiv

import test_cy
import test_py
from time_test import time_test
import test_cy_pyx


@time_test
def main_cy_pyx():
    test_cy_pyx.test(1000000)


@time_test
def main_cy():
    test_cy.test(1000000)


@time_test
def main_py():
    test_py.test(1000000)


if __name__ == '__main__':
    main_cy_pyx()
    main_cy()
    main_py()
