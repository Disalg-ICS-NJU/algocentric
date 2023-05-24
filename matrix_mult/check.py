#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Ruize Tang <tangruize97@qq.com>, Runze Wu
# <runzewu@smail.nju.edu.cn>, Anpu Lu <anpulu@smail.nju.edu.cn>.
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
from get_input import get_input  # pylint: disable=wrong-import-position # noqa
from critical_op import mult_cost  # pylint: disable=wrong-import-position, no-name-in-module # noqa
from matrix_mult import matrix_mult_dp


def check(oracle, to_check) -> bool:
    '''检查oracle和to_check是否完全一致.

    Args:
        oracle: 给定的正确结果
        to_check: 待验证的输入

    Returns:
        oracle是否与to_check完全一致的检查结果
    '''
    return oracle == to_check


def matrix_mult_check(dime_list: list, to_check: int) -> bool:
    '''检查to_check是否为正确的最小开销

    Args:
        dime_list (list): 给定的输入list
        to_check (list): 待检查的最小开销

    Returns:
        to_check是否为正确的最小开销
    '''
    return check(matrix_mult_bf(dime_list), to_check)


def matrix_mult_bf(dime_list: list) -> int:
    k = len(dime_list) - 1
    if k <= 1:
        return 0
    cost = float('inf')
    for i in range(1, k):
        cost1 = dime_list[i-1] * dime_list[i] * dime_list[i+1]
        new_list = dime_list.copy()
        new_list.pop(i)
        cost2 = matrix_mult_bf(new_list)
        cost = min(cost, cost1 + cost2)
    return cost


if __name__ == '__main__':
    testcase = get_input()
    result = matrix_mult_dp(testcase[0], testcase[1])
    if matrix_mult_check(testcase[1], result[1]):
        print('PASS')
        print('Critical op counts:', mult_cost.get_op_count())
    else:
        print('FAIL')
        print('Input :', testcase)
        print('Result:', result)
        sys.exit(1)
