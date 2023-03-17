#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Ruize Tang <tangruize97@qq.com>, Runze Wu
# <runzewu@smail.nju.edu.cn>.
#
# This file is a part of Disalg-ICS-NJU/algocentric.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from collections import Counter
from get_input import get_input  # pylint: disable=wrong-import-position # noqa
from critical_op import equal_op  # pylint: disable=wrong-import-position # noqa
from frequent_element import frequent_element


def check(oracle, to_check) -> bool:
    '''检查oracle和to_check是否完全一致.

    Args:
        oracle: 给定的正确结果
        to_check: 待验证的输入

    Returns:
        oracle是否与to_check完全一致的检查结果
    '''
    return oracle == to_check


def frequent_element_check(array: list, k: int, to_check: list) -> bool:
    '''检查to_check是否为正确的常见元素

    Args:
        array (list): 给定的输入list
        k (int): 给定的正整数常数k
        to_check (list): 待检查的常见元素序列

    Returns:
        to_check是否为正确的常见元素
    '''
    counter = Counter(array)
    oracle = [elem for elem, freq in counter.items() if freq >=
              len(array)//k+1]
    return check(sorted(oracle), to_check)


if __name__ == '__main__':
    testcase = get_input()
    result = frequent_element(testcase[0], testcase[1])
    if frequent_element_check(testcase[0], testcase[1], result):
        print('PASS')
        print('Critical op counts:', equal_op.get_op_count())
    else:
        print('FAIL')
        print('Input :', testcase)
        print('Result:', result)
        sys.exit(1)
