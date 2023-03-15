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

class CriticalOP():
    '''算法关键操作类

    我们实现的算法中, 一般都要进行某类操作来保证算法运行.
    例如排序算法中, 我们要进行两个元素的比较; 之后学到的图算法中, 往往涉及对节点或边的染色等等
    这类操作通常决定了算法的时间复杂度, 我们通过该类来维护算法关键操作的次数.
    '''

    def __init__(self):
        self.op_count = 0

    def get_op_count(self) -> int:
        '''获取关键操作的次数
        '''
        return self.op_count

    def incr_op_count(self):
        '''增加关键操作的次数
        '''
        self.op_count += 1

    def reset_op_count(self):
        '''重置关键操作的次数
        '''
        self.op_count = 0


class CompareOP(CriticalOP):
    '''比较操作类.

    对于排序算法, 两元素的大小比较是其关键操作.
    该类用于提供元素比较接口并维护比较操作的次数.
    '''

    def __call__(self, elem_a: int, elem_b: int) -> bool:
        '''排序算法中的比较操作.

        比较两元素大小, 同时记录排序算法中元素比较这一关键操作的次数, 便于性能分析.

        Args:
            elem_a (int): 待比较元素elem_a
            elem_b (int): 待比较元素elem_b

        Returns:
            bool: 若a大于b则返回True, 否则为False
        '''
        self.incr_op_count()
        return elem_a > elem_b


compare_op = CompareOP()
