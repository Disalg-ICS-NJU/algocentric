#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2025 Ruize Tang <tangruize97@qq.com>, Runze Wu
# <runzewu@smail.nju.edu.cn>, Peiyang He <peiyang_he@smail.nju.edu.cn>
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

import math
import sys
from typing import List
from critical_op import distance_op
from get_input import get_input
from point import Point
from closest_pairs import closest_pairs, brute_force


def check(oracle, to_check) -> bool:
    '''检查oracle和to_check是否完全一致.

    Args:
        oracle: 给定的正确结果
        to_check: 待验证的输入

    Returns:
        oracle是否与to_check完全一致的检查结果
    '''
    return oracle == to_check


def closest_pairs_check(array: List[Point], to_check: float) -> bool:
    '''使用O(n^2)的暴力算法检查to_check是否是点对之间的最小距离

        Args:
            array (list): 给定的输入list
            to_check (float): 待检查的点对之间的最小距离

        Returns:
            to_check是否为正确的点对之间的最小距离
    '''
    return math.isclose(brute_force(array), to_check, rel_tol=1e-9)


if __name__ == '__main__':
    testcase = get_input()
    result = closest_pairs(testcase)
    if closest_pairs_check(testcase, result):
        print('PASS')
        print('Critical op counts:', distance_op.get_op_count())
    else:
        print('FAIL')
        print('Input :', testcase)
        print('Result:', result)
        sys.exit(1)
