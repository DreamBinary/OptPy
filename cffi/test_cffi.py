# -*- coding:utf-8 -*-
# @FileName : test_cffi.py
# @Time : 2024/2/17 17:52
# @Author : fiv


import cffi


# def test(n):
#     s = 0
#     for i in range(n):
#         s += i
#     return s

# def test_cffi(n):
#     ffi = cffi.FFI()
#     ffi.cdef("long test(int);")
#     ff = ffi.verify(r"""
#     static long test(int n) {
#         long s = 0;
#         for (int i = 0; i < n; i++) {
#             s += i;
#         }
#         return s;
#     }
#     """)
#     return ff.test(n)

