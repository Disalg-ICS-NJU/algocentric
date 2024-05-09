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

import os
import sys
# 将sort目录放入python搜索路径中, 使得下面的 from ... import ... 能成功执行.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from get_input import get_input  # pylint: disable=wrong-import-position # noqa
from critical_op import equal_op  # pylint: disable=wrong-import-position, no-name-in-module # noqa


def count_frequent(array: list, target: int) -> int:
    '''计算特定元素在序列中的频率.

    Args:
        array (list): 给定序列list
        target (int): 给定序列中特定元素

    Returns:
        返回出现频率
    '''
    freq = 0
    for elem in array:
        if equal_op(elem, target):
            freq += 1
    return freq


def frequent_element(array: list, k: int) -> list:
    '''常见元素查找算法.

    Args:
        array (list): 待查找list
        k (int): 正整数常数k

    Returns:
        list: 所有常见元素的有序序列
    '''
    if k <= 0:
        assert False, "k should be positive number!"
    if len(array) <= k:
        return sorted(set(array))
    if k == 2:  # 对于k=2的情况, 我们实现了摩尔投票算法来单独处理
        return find_majority(array)

    # 对于k>2的一般情况, 采取分治思想
    # 局部常见元素可能为全局常见元素
    # 而局部不常见则必不是全局常见
    ans = set()
    mid = len(array)//2+1

    left = frequent_element(array[:mid], k)
    right = frequent_element(array[mid:], k)

    for elem in left+right:
        if count_frequent(array, elem) >= len(array)//k+1:
            ans.add(elem)

    return sorted(ans)


def find_majority(array: list) -> list:
    '''摩尔投票寻找大多数算法

    Args:
        array (list): 待查找list

    Returns:
        返回包含大多数的列表, 不存在返回空
    '''
    major, freq = 0, 0
    for elem in array:
        if freq == 0:
            major = elem
        if equal_op(elem, major):
            freq += 1
        else:
            freq -= 1
    if count_frequent(array, major) >= len(array)//2+1:
        return [major]
    return []


if __name__ == '__main__':
    testcase = get_input()
    result = frequent_element(testcase[0], testcase[1])
    print(' '.join(map(str, result)))
