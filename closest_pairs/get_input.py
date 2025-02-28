# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Ruize Tang <tangruize97@qq.com>, Runze Wu
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

from typing import List
from point import Point


def get_input() -> List[Point]:
    '''从标准输入获取输入, 第一行是点的数量n, 下面n行每行由一个空格分隔的两个整数组成, 代表点的横纵坐标

    Returns:
        点结构体组成的列表
    '''
    n = int(input().strip())
    points = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        points.append(Point(x, y))
    return points
