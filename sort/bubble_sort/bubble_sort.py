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


def bubble_sort(array: list, optimize=False) -> list:
    '''冒泡排序算法.

    Args:
        array (list): 未排序的list
        optimize (bool, optional): 是否为优化冒泡排序算法. 默认为无优化版本

    Returns:
        返回排序后的list
    '''

    new_list = list(array)
    for i in range(len(new_list)-1):
        flag = False
        for j in range(0, len(new_list)-i-1):
            if compare_op(new_list[j], new_list[j+1]):
                flag = True
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
        if optimize and flag is False:  # 优化版本, 当一轮没有发生交换元素时, 算法即可终止.
            break
    return new_list


if __name__ == '__main__':
    testcase = get_input()
    result = bubble_sort(testcase)
    print(' '.join(map(str, result)))
