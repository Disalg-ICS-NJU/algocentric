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

from collections import defaultdict
import os
import sys
from critical_op import compare_op  # pylint: disable=wrong-import-position, no-name-in-module # noqa
# 将prim目录放入python搜索路径中, 使得下面的 from ... import ... 能成功执行.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from get_input import get_input  # pylint: disable=wrong-import-position # noqa
from min_heap import MinHeap  # pylint: disable=wrong-import-position # noqa
from node import Node  # pylint: disable=wrong-import-position # noqa


def dijkstra(node_num: int,start: int, edges: list[tuple]) -> int:
    '''采用最小堆实现的dijkstra算法

    Args:
        node_num (int): 图的节点数
        start (int): 源节点
        edges (list[tuple]): 图所有的边

    Returns:
        从源节点到所有点的最短路径长度
    '''
    adjacent_dict = defaultdict(list[Node])  # 注意：defaultdict(list)必须以list做为变量
    for node_1, node_2, weight in edges:
        adjacent_dict[node_1].append(Node(node_2, node_1, weight))
        #adjacent_dict[node_2].append(Node(node_1, node_2, weight)) #无向图则取消该注释

    visited = [False for _ in range(node_num)]  # 是否访问过该节点
    visited[start] = True
    dij_node = {start}  # 当前确定的最短路径目标节点
    results=[0x7fffffff for _ in range(node_num)]
    results[start]=0
    heap = MinHeap(node_num)
    for neighbor in adjacent_dict[start]:
        neighbor.dist=results[start]+neighbor.weight
        heap.insert(neighbor)
        visited[neighbor.node_id] = True

    while compare_op(len(heap) , 0):
        node = heap.extract_min()
        dij_node.add(node.node_id)  # 该节点加入dij_node
        results[node.node_id]=node.dist
        for neighbor in adjacent_dict[node.node_id]:
            if visited[neighbor.node_id] is False:  # 尚未访问过该节点
                neighbor.dist=results[neighbor.point_to]+neighbor.weight
                heap.insert(neighbor)
                visited[neighbor.node_id] = True
            elif neighbor.node_id not in dij_node:  # 节点在Fringe中, 考虑更新其权重
                if compare_op(neighbor.dist,neighbor.weight+results[neighbor.point_to]):
                    neighbor.dist=neighbor.weight+results[neighbor.point_to]
                    heap.decrease_key(neighbor)
            elif compare_op(results[neighbor.node_id],neighbor.weight+results[neighbor.point_to]):
                neighbor.dist=neighbor.weight+results[neighbor.point_to]
                if heap.node_pos[neighbor.node_id]==-1:
                    heap.insert(neighbor)
                else:
                    heap.decrease_key(neighbor)

    return results


if __name__ == '__main__':
    testcase = get_input()
    result = dijkstra(testcase[0], testcase[1], testcase[2])
    print(*result)
