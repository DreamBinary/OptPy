# -*- coding:utf-8 -*-
# @FileName : setup.py
# @Time : 2024/2/13 14:30
# @Author : fiv

from distutils.core import setup
from Cython.Build import cythonize
import numpy as np
import pydub

# setup(
#     ext_modules=cythonize(["test_cy_pyx.pyx"])
# )
setup(
    ext_modules=cythonize(["slice_pyx.pyx"]),
    # from pydub import AudioSegment
    # from pydub.utils import make_chunks
    install_requires=["pydub", "pathlib", "multiprocessing"],
)
# python setup.py build_ext --inplace
