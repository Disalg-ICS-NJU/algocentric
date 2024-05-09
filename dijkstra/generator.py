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
from random import choice
from random import sample
import argparse



def get_random_graph(node_num: int, edge_num: int, min_w: int, max_w: int) \
        -> list:
    '''获取随机生成的非负权权无向连通图

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
    edge_size=0
    node_pair = set()
    used_nodes = set()
    unused_nodes = set(nodes)

    # 先添加n-1条边, 保证图连通
    while edge_size < node_num-1:
        if edge_size == 0:  # 生成第一条边
            node_1 = randint(0, node_num-2)
            node_2 = randint(node_1+1, node_num-1)
            used_nodes = used_nodes.union((node_1, node_2))
            unused_nodes = unused_nodes-{node_1, node_2}
            edges[node_1][node_2]=randint(min_w, max_w)
            node_pair.add((node_1, node_2))
            edge_size += 1
        else:  # 生成剩余的n-2条边
            node_1 = choice(list(used_nodes))
            node_2 = choice(list(unused_nodes))
            used_nodes.add(node_2)
            unused_nodes.remove(node_2)
            if node_2 < node_1:
                node_1, node_2 = node_2, node_1
            edges[node_1][node_2]=randint(min_w, max_w)
            node_pair.add((node_1, node_2))
            edge_size += 1

    # 添加剩余的m-n+1条边
    while edge_size < edge_num:
        node_1 = randint(0, node_num-2)
        node_2 = randint(node_1+1, node_num-1)
        if (node_1, node_2) not in node_pair:
            edges[node_1][node_2]=randint(min_w, max_w)
            node_pair.add((node_1, node_2))
            edge_size+=1

    return edges

def get_negative_edges(node_num: int,edges: list) \
    -> list:
    # 随机生成负权环的顶点
    cycle_nodes=sample(range(0, node_num),2)
    node_1=cycle_nodes[0]
    node_2=cycle_nodes[1]
    edges[node_1][node_2]=-1
    edges[node_2][node_1]=0
    #print(node_1,node_2,edges[node_1][node_2])

    return edges

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
    #先生成一个不含负权边的无向连通图
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
        min_edge_number = max(args.min,node_number)
        max_edge_number = min(min_edge_number+1,args.max,node_number*(node_number-1)/2)
        edge_number = randint(min_edge_number,max_edge_number)
        edge_list = get_random_input(
            node_number, edge_number, args.has_negative_edges, args.has_negative_cycle)
        print(node_number, len(edge_list),randint(1,node_number-1))
        for edge in edge_list:
            print(' '.join(map(str, edge)))
