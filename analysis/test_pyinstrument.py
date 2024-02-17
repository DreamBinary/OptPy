# -*- coding:utf-8 -*-
# @FileName : test_pyinstrument.py
# @Time : 2024/2/17 20:07
# @Author : fiv

from pyinstrument import Profiler

from julia import test_julia

profiler = Profiler()
profiler.start()
test_julia()
profiler.stop()
print(profiler.output_text(unicode=True, color=True))
