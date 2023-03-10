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

import bubble_sort
import sys

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
    testcase = bubble_sort.get_input()
    result = bubble_sort.bubble_sort(testcase)
    if sort_check(testcase, result):
        print('PASS')
        print('Before optimization, critial op counts:',
              bubble_sort.CRITICAL_OP_COUNTS)
        if len(sys.argv)>1 and sys.argv[1]=='optimize':
            bubble_sort.CRITICAL_OP_COUNTS = 0
            bubble_sort.bubble_sort(testcase, True)
            print('After optimization, critial op counts :',
                bubble_sort.CRITICAL_OP_COUNTS)
    else:
        print('FAIL')
        print('Input :', testcase)
        print('Result:', result)
        exit(1)
