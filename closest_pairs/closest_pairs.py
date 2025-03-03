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
from point import Point  # pylint: disable=wrong-import-position, no-name-in-module # noqa
from get_input import get_input  # pylint: disable=wrong-import-position, no-name-in-module # noqa
from critical_op import DistanceOP  # pylint: disable=wrong-import-position, no-name-in-module # noqa


def brute_force(array: List[Point], distance_op: DistanceOP) -> (float, int):
    # O(n^2)的暴力算法, 枚举每一个可能的点对距离
    n = len(array)
    min_distance = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance_op(array[i], array[j])
            min_distance = min(min_distance, dist)
    return min_distance, distance_op.get_op_count()


def closest_pairs_recursion(array: List[Point], distance_op: DistanceOP) -> float:
    n = len(array)
    if n <= 3:
        # 对于n<=3的情况, 使用暴力算法直接求解
        return brute_force(array, distance_op)[0]
    mid = n // 2
    mid_point = array[mid]
    l = closest_pairs_recursion(array[:mid], distance_op)
    r = closest_pairs_recursion(array[mid:], distance_op)
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


def divide_and_conquer(array: List[Point]) -> (float, int):
    array = sorted(array, key=lambda p: p.x)
    distance_op = DistanceOP()
    return closest_pairs_recursion(array, distance_op), distance_op.get_op_count()


def closest_pairs(array: List[Point]) -> (float, int):
    # 你可以修改 closet_pairs 为你的实现, 但请保持函数签名不变
    # 第一个返回值返回点对之间的最小距离, 第二个返回值返回关键操作(求距离)的次数
    # 求取两个 Point 之间的距离时, 请调用 distance_op 方法, 例如:
    # distance_op = DistanceOP()
    # dist = distance_op(p, q)
    # 由于 DistanceOP 实例内部维护了计数值, 因此请确保在你的实现中只创建了一个 DistanceOP 实例
    return divide_and_conquer(array)


if __name__ == '__main__':
    testcase = get_input()
    result = closest_pairs(testcase)
    print(result[0])
