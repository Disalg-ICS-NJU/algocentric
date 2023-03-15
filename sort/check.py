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
import argparse
from common import get_input, compare_op


def check(oracle, to_check) -> bool:
    '''检查oracle和to_check是否完全一致.

    Args:
        oracle: 给定的正确结果
        to_check: 待验证的输入

    Returns:
        oracle是否与to_check完全一致的检查结果
    '''
    return oracle == to_check


def sort_check(array: list, to_check: list) -> bool:
    '''检查给定to_check是否为array排序后的结果.

    Args:
        array (list): 未排序的原始输入list
        to_check (list): 待检查的list

    Returns:
        to_check是否为array排序后的结果
    '''
    oracle = sorted(list(array))
    return check(oracle, to_check)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test sort algorithm")
    parser.add_argument('-o', dest='optimize', action='store_true',
                        help="enable optimization for bubble_sort")
    parser.add_argument(dest='target', default='bubble_sort', nargs='?',
                        help="target dir")
    args = parser.parse_args()
    if args.target == 'bubble_sort':
        import bubble_sort
        from functools import partial
        sort = partial(bubble_sort.sort, optimize=args.optimize)
    else:
        sort = __import__(args.target).sort

    testcase = get_input()
    result = sort(testcase)
    if sort_check(testcase, result):
        print('PASS')
        print('Critical op counts:', compare_op.get_op_count())
    else:
        print('FAIL')
        print('Input :', testcase)
        print('Result:', result)
        sys.exit(1)
