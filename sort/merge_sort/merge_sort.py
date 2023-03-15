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
import os
# 将sort目录放入python搜索路径中, 使得下面的 from common import ... 能成功执行.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common import get_input, compare_op  # pylint: disable=wrong-import-position # noqa


def merge_sort(array: list) -> list:
    '''归并排序算法.

    Args:
        array (list): 未排序的list

    Returns:
        返回排序后的list
    '''

    num = len(array)
    if num <= 1:
        return list(array)
    left = merge_sort(array[:num//2])
    right = merge_sort(array[num//2:])
    new_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare_op(left[i], right[j]):
            new_list.append(right[j])
            j += 1
        else:
            new_list.append(left[i])
            i += 1
    new_list += left[i:] + right[j:]
    return new_list


if __name__ == '__main__':
    testcase = get_input()
    result = merge_sort(testcase)
    print(' '.join(map(str, result)))
