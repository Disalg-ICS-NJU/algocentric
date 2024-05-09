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

class Node:
    '''节点类

    记录每个节点在Fringe中的权重
    '''

    def __init__(self, node_id: int, point_to: int, weight: int):
        '''生成一个节点Node

        Args:
            id (int): 节点的id
            point_to(int): 指向的节点
            weight (int): 边的权重
        '''
        self.node_id = node_id
        self.point_to = point_to
        self.weight = weight
        self.dist= 0x7fffffff

    def __lt__(self, other) -> bool:
        '''实现__lt__自定义比较'''
        return self.dist < other.dist

    def __repr__(self) -> str:
        return f'{self.node_id}:{self.point_to} weight:{self.weight} dist:{self.dist}'
