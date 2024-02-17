# -*- coding:utf-8 -*-
# @FileName : test_cProfile.py
# @Time : 2024/2/17 19:42
# @Author : fiv

import cProfile
from julia import calc_pure_python


def profile_me():
    calc_pure_python(draw_output=False, desired_width=1000, max_iterations=300)


if __name__ == '__main__':
    profile = cProfile.Profile()
    profile.runcall(profile_me)
    profile.print_stats()

"""
ncalls: the number of calls made.
tottime: the total time spent in the given function (excluding time made in calls to sub-functions).
percall: the quotient of tottime divided by ncalls.
cumtime: the total time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.   
percall: the quotient of cumtime divided by primitive calls.
filename:lineno(function): the function name, filename, and line number of the call.
"""

# calculate_z_serial_purepython took 9.42720079421997 seconds
#          36221994 function calls in 9.996 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    6.992    6.992    9.427    9.427 julia.py:15(calculate_z_serial_purepython)
#         1    0.447    0.447    9.971    9.971 julia.py:29(calc_pure_python)
#         1    0.025    0.025    9.996    9.996 test_cProfile.py:10(profile_me)
#  34219980    2.436    0.000    2.436    0.000 {built-in method builtins.abs}
#         4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.005    0.005    0.005    0.005 {built-in method builtins.sum}
#         2    0.000    0.000    0.000    0.000 {built-in method time.time}
#   2002000    0.092    0.000    0.092    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
