#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Ruize Tang <tangruize97@qq.com>, Runze Wu
# <runzewu@smail.nju.edu.cn>, Jingbo Zhai <306330361@qq.com>
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
from critical_op import compare_op  # pylint: disable=wrong-import-position, no-name-in-module # noqa
from bellmanford import bellman_ford
from dijkstra import dijkstra


def check(oracle, to_check) -> bool:
    '''检查oracle和to_check是否完全一致.

    Args:
        oracle: 给定的正确结果
        to_check: 待验证的输入

    Returns:
        oracle是否与to_check完全一致的检查结果
    '''
    if len(oracle)!=len(to_check):
        return False
    if oracle!=to_check:
        return False
    return True


if __name__ == '__main__':
    testcase = get_input()
    result = dijkstra(testcase[0], testcase[1], testcase[2])
    ref = bellman_ford(testcase[0],testcase[1],testcase[2])

    if check(ref, result):
        print('PASS')
        print('Critical op counts:', compare_op.get_op_count())
    else:
        print('FAIL')
        print('Input :', testcase)
        for i, j in zip(ref, result):
            print(i, j)
        sys.exit(1)
