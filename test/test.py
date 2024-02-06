# -*- coding:utf-8 -*-
# @FileName : test.py
# @Time : 2024/2/6 16:53
# @Author : fiv

def test():
    import time
    import numpy as np
    start = time.time()
    a = np.random.rand(1000000)
    b = np.random.rand(1000000)
    c = np.dot(a, b)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    test()
