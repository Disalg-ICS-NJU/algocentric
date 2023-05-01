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

from random import randint
from random import choice
import argparse


def get_random_input(node_num: int, edge_num: int, min_w: int, max_w: int) \
        -> list:
    '''获取随机生成的加权无向连通图

    Args:
        node_num(int): 图的节点数
        edge_num(int): 图的边数
        min_w(int): 边权重最小值
        max_w(int): 边权重最大值

    Returns:
        图上所有边
    '''
    nodes = list(range(node_num))
    edges = []
    node_pair = set()

    used_nodes = set()
    unused_nodes = set(nodes)

    # 先添加n-1条边, 保证图连通
    while len(edges) < node_num-1:
        if len(edges) == 0:  # 生成第一条边
            node_1 = randint(0, node_num-2)
            node_2 = randint(node_1+1, node_num-1)
            used_nodes = used_nodes.union((node_1, node_2))
            unused_nodes = unused_nodes-{node_1, node_2}
            edges.append((node_1, node_2, randint(min_w, max_w)))
            node_pair.add((node_1, node_2))
        else:  # 生成剩余的n-2条边
            node_1 = choice(list(used_nodes))
            node_2 = choice(list(unused_nodes))
            used_nodes.add(node_2)
            unused_nodes.remove(node_2)
            if node_2 < node_1:
                node_1, node_2 = node_2, node_1
            edges.append((node_1, node_2, randint(min_w, max_w)))
            node_pair.add((node_1, node_2))

    # 添加剩余的m-n+1条边
    while len(edges) < edge_num:
        node_1 = randint(0, node_num-2)
        node_2 = randint(node_1+1, node_num-1)
        if (node_1, node_2) not in node_pair:
            edges.append((node_1, node_2, randint(min_w, max_w)))
            node_pair.add((node_1, node_2))

    return edges


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Genrate random test inputs")
    parser.add_argument('-n', dest='min_node', type=int, default=5,
                        help="min node number")
    parser.add_argument('-N', dest='max_node', type=int, default=100,
                        help="max node number")
    parser.add_argument('-m', dest='min', type=int, default=10,
                        help="min edge number")
    parser.add_argument('-M', dest='max', type=int, default=50000,
                        help="max edge number")
    parser.add_argument('-w', dest='min_w', type=int, default=2,
                        help="min edge weight")
    parser.add_argument('-W', dest='max_w', type=int, default=20,
                        help="max edge weight")
    parser.add_argument(dest='num', type=int, default=10, nargs='?',
                        help="number of test input")
    args = parser.parse_args()
    for _ in range(args.num):
        node_number = randint(args.min_node, args.max_node)
        edge_number = randint(min(args.min, node_number*2-1),
                              min(args.max, node_number*2-1))
        edge_list = get_random_input(
            node_number, edge_number, args.min_w, args.max_w)
        print(node_number, len(edge_list))
        for edge in edge_list:
            print(' '.join(map(str, edge)))
