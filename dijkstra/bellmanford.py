#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Jingbo Zhai <306330361@qq.com>
# 
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

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from get_input import get_input  # pylint: disable=wrong-import-position # noqa

# 单源最短路的正确性判定，使用 Bellman-Ford 算法
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        #self.graph.append([v, u, w])  # 对于含负权的无向图，不能使用bellman-ford

    def bellman_ford(self, src):
        dist = [0x7fffffff] * self.V
        dist[src] = 0

        # 松弛操作，重复执行 V-1 次
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != 0x7fffffff and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # 检查负权环
        for u, v, w in self.graph:
            if dist[u] != 0x7fffffff and dist[u] + w < dist[v]:
                print("图中存在负权环")
                return dist

        # 如果不存在负权环，则打印最短路径
        return dist

def Bellman_ford(node_num: int,src: int,edges: list[tuple]):
    g = Graph(node_num)

    # 添加边
    for u,v,w in edges:
        g.add_edge(u,v,w)

    # 运行贝尔曼-福特算法
    return g.bellman_ford(src)

if __name__ == '__main__':
    testcase = get_input()
    result = Bellman_ford(testcase[0], testcase[1], testcase[2])
    print(*result)


