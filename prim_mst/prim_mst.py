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

from collections import defaultdict
import os
import sys
# 将prim目录放入python搜索路径中, 使得下面的 from ... import ... 能成功执行.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from get_input import get_input  # pylint: disable=wrong-import-position # noqa
from min_heap import MinHeap  # pylint: disable=wrong-import-position # noqa
from node import Node  # pylint: disable=wrong-import-position # noqa


def prim(node_num: int, edges: list[tuple]) -> int:
    '''采用最小堆实现的prim算法

    Args:
        node_num (int): 图的节点数
        edges (list[tuple]): 图所有的边

    Returns:
        最小生成树对应的权重
    '''
    adjacent_dict = defaultdict(list[Node])  # 注意：defaultdict(list)必须以list做为变量
    for node_1, node_2, weight in edges:
        adjacent_dict[node_1].append(Node(node_2, node_1, weight))
        adjacent_dict[node_2].append(Node(node_1, node_2, weight))

    start = 0  # 以编号为0的节点作为Prim算法起始点
    visited = [False for _ in range(node_num)]  # 是否访问过该节点
    visited[0] = True
    total_weight = 0  # mst的权重
    mst_node = {0}  # 当前mst中具有的节点

    heap = MinHeap()
    for neighbor in adjacent_dict[start]:
        heap.insert(neighbor)
        visited[neighbor.node_id] = True

    while len(heap) > 0 and len(mst_node) < node_num:
        node = heap.extract_min()
        mst_node.add(node.node_id)  # 该节点加入mst
        total_weight += node.weight  # 加入该节点的权重
        for neighbor in adjacent_dict[node.node_id]:
            if visited[neighbor.node_id] is False:  # 尚未访问过该节点
                heap.insert(neighbor)
                visited[neighbor.node_id] = True
            elif neighbor.node_id not in mst_node:  # 节点在Fringe中, 考虑更新其权重
                heap.decrease_key(neighbor)

    assert len(mst_node) == node_num  # 连通图总能找到生成树
    return total_weight


if __name__ == '__main__':
    testcase = get_input()
    result = prim(testcase[0], testcase[1])
    print(result)
