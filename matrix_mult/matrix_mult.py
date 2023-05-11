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

import os
import sys

# 将matrix目录放入python搜索路径中, 使得下面的 from ... import ... 能成功执行.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from get_input import get_input  # pylint: disable=wrong-import-position # noqa
from critical_op import mult_cost  # pylint: disable=wrong-import-position, no-name-in-module # noqa


def matrix_mult_dp(k: int, dime_list: list) -> (str, int):
    '''计算矩阵连乘结果.

    Args:
        k (int): 矩阵个数
        dime_list (list): 给定矩阵信息list

    Returns:
        返回最优顺序连乘和最小结果
    '''
    cost = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
    last = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
    for low in range(k - 1, -1, -1):
        for high in range(low + 1, k + 1):
            if high - low == 1:
                best_cost = 0
                best_last = -1
            else:
                best_cost = float('inf')
                best_last = low
            for mid in range(low + 1, high):
                cost0 = cost[low][k]
                cost1 = cost[k][high]
                cost2 = mult_cost(dime_list[low], dime_list[mid], dime_list[high])
                if cost0 + cost1 + cost2 < best_cost:
                    best_cost = cost0 + cost1 + cost2
                    best_last = mid
            cost[low][high] = best_cost
            last[low][high] = best_last
    return extract_order(last, k), cost[0][k]


def extract_order(last: list, k: int) -> str:
    '''求连乘顺序.

    Args:
        last (list): DP计算结果
        k (int): 矩阵个数n

    Returns:
        list: 最终连乘顺序
    '''
    que_mult_order = ""
    que_mult_order = extract(que_mult_order, last, 0, k)
    return que_mult_order


def extract(que_mult_order: str, last: list, low: int, high: int) -> str:
    '''求连乘顺序的具体操作.

    Args:
        que_mult_order (str): 待生成结果
        last (list): DP计算结果
        low (int): 子序列头下标
        high (int): 子序列尾下标

    Returns:
        str: 连乘顺序
    '''
    if high - low > 1:
        que_mult_order += '('
        k = last[low][high]
        que_mult_order = extract(que_mult_order, last, low, k)
        que_mult_order = extract(que_mult_order, last, k, high)
        que_mult_order += ')'
    else:
        que_mult_order += 'A[' + str(low) + ']'
    return que_mult_order


if __name__ == '__main__':
    testcase = get_input()
    result = matrix_mult_dp(testcase[0], testcase[1])
    print(result[0])
    print(result[1])
