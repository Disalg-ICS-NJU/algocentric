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
from collections import defaultdict
from get_input import get_input  # pylint: disable=wrong-import-position # noqa
from node import Node  # pylint: disable=wrong-import-position # noqa
from critical_op import compare_op  # pylint: disable=wrong-import-position, no-name-in-module # noqa
from prim_mst import prim


def check(oracle, to_check) -> bool:
    '''检查oracle和to_check是否完全一致.

    Args:
        oracle: 给定的正确结果
        to_check: 待验证的输入

    Returns:
        oracle是否与to_check完全一致的检查结果
    '''
    return oracle == to_check


def mst_weight_check(node_num: int, edges: list[tuple], to_check: int) -> bool:
    '''检查to_check是否为最小权重和, 采用遍历数组找最值的实现方法

    Args:
        node_num (int): 图的节点数
        edges (list[tuple]): 图所有的边
        to_check (int): 待检查的权重和

    Returns:
        to_check是否为最小权重和
    '''
    max_weight = 0  # 最大的边权重
    adjacent_dict = defaultdict(list[Node])  # 注意：defaultdict(list)必须以list做为变量
    for node_1, node_2, weight in edges:
        max_weight = max(max_weight, weight)
        adjacent_dict[node_1].append(Node(node_2, node_1, weight))
        adjacent_dict[node_2].append(Node(node_1, node_2, weight))

    start = 0  # 以编号为0的节点作为Prim算法起始点
    visited = [False for _ in range(node_num)]  # 是否访问过该节点
    visited[0] = True
    oracle = 0  # mst的权重
    mst_node = {0}  # 当前mst中具有的节点

    # 所有节点的权重均为最大, 保证不被选取
    node_weight = [Node(-1, -1, max_weight+1) for _ in range(node_num)]
    for neighbor in adjacent_dict[start]:
        node_weight[neighbor.node_id] = neighbor
        visited[neighbor.node_id] = True

    while len(mst_node) < node_num:
        node = min(node_weight)  # 遍历找去权重最小的
        mst_node.add(node.node_id)  # 该节点加入mst
        oracle += node.weight  # 加入该节点的权重
        node_weight[node.node_id].weight = max_weight+1  # 保证不再被选取
        for neighbor in adjacent_dict[node.node_id]:
            if visited[neighbor.node_id] is False:  # 尚未访问过该节点
                node_weight[neighbor.node_id] = neighbor
                visited[neighbor.node_id] = True
            elif neighbor.node_id not in mst_node:  # 节点在Fringe中, 考虑更新其权重
                if node_weight[neighbor.node_id].weight > neighbor.weight:
                    node_weight[neighbor.node_id] = neighbor

    return check(oracle, to_check)


if __name__ == '__main__':
    testcase = get_input()
    result = prim(testcase[0], testcase[1])
    if mst_weight_check(testcase[0], testcase[1], result):
        print('PASS')
        print('Critical op counts:', compare_op.get_op_count())
    else:
        print('FAIL')
        print('Input :', testcase)
        print('Result:', result)
        sys.exit(1)
