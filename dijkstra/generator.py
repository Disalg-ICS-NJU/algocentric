#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Ruize Tang <tangruize97@qq.com>, Runze Wu
# <runzewu@smail.nju.edu.cn>, Jingbo Zhai <306330361@qq.com>.
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
from random import sample
from random import shuffle
import copy
import argparse
from bellmanford import bellman_ford



def get_random_graph(node_num: int, edge_num: int, min_w: int, max_w: int) \
        -> list:
    '''获取随机生成的非负权有向连通图

    Args:
        node_num(int): 图的节点数
        edge_num(int): 图的边数
        min_w(int): 边权重最小值
        max_w(int): 边权重最大值

    Returns:
        图的邻接矩阵
    '''
    nodes = list(range(node_num))
    edges = [[0 for _ in range(node_num)] for _ in range(node_num)]
    edge_size = 0
    node_pair = set()

    # 保证图的连通性，先生成一个包含所有节点的随机环
    shuffle(nodes)
    for i in range(node_num):
        node_1 = nodes[i]
        node_2 = nodes[(i + 1) % node_num]
        weight = randint(min_w, max_w)
        edges[node_1][node_2] = weight
        node_pair.add((node_1, node_2))
        edge_size += 1

    # 添加剩余的边直到达到edge_num
    while edge_size < edge_num:
        node_1 = randint(0, node_num - 1)
        node_2 = randint(0, node_num - 1)
        if node_1 != node_2 and (node_1, node_2) not in node_pair:
            weight = randint(min_w, max_w)
            edges[node_1][node_2] = weight
            node_pair.add((node_1, node_2))
            edge_size += 1

    return edges

def get_negative_edges(node_num: int,edges: list) \
    -> list:
    new_edges = copy.deepcopy(edges)

    for _ in range(randint(1, 20)):
        while True:
            temp_edges = copy.deepcopy(new_edges)
            cycle_nodes = sample(range(0, node_num), 2)

            node_1 = cycle_nodes[0]
            node_2 = cycle_nodes[1]
            temp_edges[node_1][node_2] = randint(-20, -1)

            result_edgeslist = []
            for i in range(node_num):
                for j in range(node_num):
                    if temp_edges[i][j] != 0:
                        result_edgeslist.append((i, j, temp_edges[i][j]))

            if bellman_ford(node_num, 0, result_edgeslist) is not None:
                new_edges = temp_edges
                break
    return new_edges

def get_negative_cycle(node_num: int,edges: list) \
    -> list:
    # 随机生成负权环的顶点
    cycle_nodes=sample(range(0, node_num), randint(3,node_num))
    node_1=cycle_nodes[-1]
    node_2=cycle_nodes[0]
    edges[node_1][node_2]=randint(-20,-2)
    edges[node_2][node_1]=0
    #print(node_1,node_2,edges[node_1][node_2])
    for i in range(len(cycle_nodes) - 1):
        node_1=cycle_nodes[i]
        node_2=cycle_nodes[i+1]
        edges[node_1][node_2]=randint(-20,-2)
        edges[node_2][node_1]=0
        #print(node_1,node_2,edges[node_1][node_2])
    return edges

def get_random_input(node_num: int, edge_num: int,
                     has_negative_edges: bool = False,
                     has_negative_cycle: bool = False) \
        -> list:

    min_weight=2
    max_weight=20
    #先生成一个不含负权边的有向连通图
    edges = get_random_graph(node_num, edge_num, min_weight, max_weight)

    if has_negative_cycle:
        edges= get_negative_cycle(node_num,edges)
    elif has_negative_edges:
        edges= get_negative_edges(node_num,edges)

    result_edgeslist= []
    for i in range(0,node_num):
        for j in range(0,node_num):
            if edges[i][j]:
                result_edgeslist.append((i,j,edges[i][j]))
    return result_edgeslist


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Genrate random test inputs")
    parser.add_argument('-n', dest='min_node', type=int, default=5,
                        help="min node number")
    parser.add_argument('-N', dest='max_node', type=int, default=100,
                        help="max node number")
    parser.add_argument('-m', dest='min', type=int, default=10,
                        help="min edge number")
    parser.add_argument('-M', dest='max', type=int, default=500,
                        help="max edge number")
    parser.add_argument(dest='num', type=int, default=1, nargs='?',
                        help="number of test input")
    parser.add_argument("--has_negative_edges", action="store_true",
                        help="Whether the graph can have negative edges")
    parser.add_argument("--has_negative_cycle", action="store_true",
                        help="Whether the graph can have negative cycles")

    args = parser.parse_args()
    for _ in range(args.num):
        node_number = randint(args.min_node, args.max_node)
        max_edge_number = min(args.min,args.max,node_number*(node_number-1)/2)
        min_edge_number = min(args.min,node_number,max_edge_number)
        edge_number = randint(min_edge_number,max_edge_number)
        edge_list = get_random_input(
            node_number, edge_number, args.has_negative_edges, args.has_negative_cycle)
        print(node_number, len(edge_list),randint(1,node_number-1))
        for edge in edge_list:
            print(' '.join(map(str, edge)))
