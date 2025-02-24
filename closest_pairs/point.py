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

import math


class Point:
    '''二维平面上的点类'''

    def __init__(self, x: int, y: int):
        '''生成一个点Point

        Args:
            x: 点的横坐标
            y: 点的纵坐标
        '''
        self.x = x
        self.y = y

    def distance(self, other) -> float:
        """计算两个点的欧几里得距离"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return f'Point({self.x}, {self.y})'
