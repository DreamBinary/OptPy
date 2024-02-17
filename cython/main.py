# -*- coding:utf-8 -*-
# @FileName : main.py
# @Time : 2024/2/13 14:28
# @Author : fiv


from time_test import time_test


def test():
    import test_cy
    import test_py
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

    main_cy_pyx()
    main_cy()
    main_py()


def test_slice():
    from pathlib import Path
    import slice_pyx
    import slice
    @time_test
    def test_slice():
        slice.slice_wav(Path("test.wav"), 30000)

    @time_test
    def test_slice_pyx():
        slice_pyx.slice_wav(Path("test.wav"), 30000)

    test_slice()
    test_slice_pyx()


if __name__ == '__main__':
    # import slice_pyx
    # print(dir(slice_pyx))
    test_slice()
