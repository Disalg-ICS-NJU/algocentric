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

def get_input() -> tuple[int, int, list[tuple]]:
    '''从标准输入获取加权有向图和源点

    Returns:
        图的节点数，源节点和所有边
    '''
    node_num, edge_num, start = map(int, input().split())
    edges = []
    for _ in range(edge_num):
        edges.append(tuple(map(int, input().split())))

    return node_num, start, edges
