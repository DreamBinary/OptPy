# -*- coding:utf-8 -*-
# @FileName : setup.py
# @Time : 2024/2/13 14:30
# @Author : fiv

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["test_cy_pyx.pyx"])
)
# python setup.py build_ext --inplace
