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
        self.vertices = vertices
        self.graph = []

    def add_edge(self, vertice, point_to, weight):
        self.graph.append([vertice, point_to, weight])
        #self.graph.append([v, u, w])  # 对于含负权的无向图，不能使用bellman-ford

    def bellman_ford(self, src):
        dist = [0x7fffffff] * self.vertices
        dist[src] = 0

        # 松弛操作，重复执行 V-1 次
        for _ in range(self.vertices - 1):
            for vertice, point_to, weight in self.graph:
                if dist[vertice] != 0x7fffffff and dist[vertice] + weight < dist[point_to]:
                    dist[point_to] = dist[vertice] + weight

        # 检查负权环
        for vertice, point_to, weight in self.graph:
            if dist[vertice] != 0x7fffffff and dist[vertice] + weight < dist[point_to]:
                return None
        # 如果不存在负权环，则打印最短路径
        return dist

def bellman_ford(node_num: int,src: int,edges: list[tuple]):
    graph = Graph(node_num)

    # 添加边
    for vertice, point_to, weight in edges:
        graph.add_edge(vertice, point_to, weight)

    # 运行贝尔曼-福特算法
    return graph.bellman_ford(src)

if __name__ == '__main__':
    testcase = get_input()
    result,opcnt = bellman_ford(testcase[0], testcase[1], testcase[2])
    if result is None:
        print("检测到负权环")
    else:
        print("源点到所有点的最短路径距离：", result)
