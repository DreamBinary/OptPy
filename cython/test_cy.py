# -*- coding:utf-8 -*-
# @FileName : test_cy.py
# @Time : 2024/2/13 14:40
# @Author : fiv
import cython


def test(n: cython.int):
    s: cython.int = 0
    for i in range(n):
        s += i
    return s
