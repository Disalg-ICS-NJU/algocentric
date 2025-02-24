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

import os
import sys
from typing import List

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from point import Point
from get_input import get_input
from critical_op import distance_op


def brute_force(array: List[Point]) -> float:
    # O(n^2)的暴力算法, 枚举每一个可能的点对距离
    n = len(array)
    min_distance = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance_op(array[i], array[j])
            min_distance = min(min_distance, dist)
    return min_distance


def closest_pairs_recursion(array: List[Point]) -> float:
    n = len(array)
    if n <= 3:
        # 对于n<=3的情况, 使用暴力算法直接求解
        return brute_force(array)
    mid = n // 2
    mid_point = array[mid]
    l = closest_pairs_recursion(array[:mid])
    r = closest_pairs_recursion(array[mid:])
    delta = min(l, r)
    ans = delta
    # 处理跨越中间点的情形
    slab = []
    for _, point in enumerate(array):
        if abs(point.x - mid_point.x) <= delta:
            slab.append(point)
    slab = sorted(slab, key=lambda p: p.y)
    for (i, point) in enumerate(slab):
        for j in range(i + 1, min(len(slab), i + 8)):
            ans = min(ans, distance_op(point, slab[j]))
    return ans


def closest_pairs(array: List[Point]) -> float:
    array = sorted(array, key=lambda p: p.x)
    return closest_pairs_recursion(array)


if __name__ == '__main__':
    testcase = get_input()
    result = closest_pairs(testcase)
    print(result)
