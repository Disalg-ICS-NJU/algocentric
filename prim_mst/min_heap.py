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

from node import Node
from critical_op import compare_op  # pylint: disable=wrong-import-position, no-name-in-module # noqa


class MinHeap:
    '''最小堆

    最小堆中的元素为我们的节点Node类.
    为了保证decrease_key操作在O(log n)时间完成, 我们维护了节点到堆中对应位置的映射.
    '''

    def __init__(self, node_num: int):
        '''堆和位置映射初始化'''
        # 采用数组存储堆
        self.heap = []
        # 采用数组结构记录节点id对应在堆中数组的下标, 访问存取均为O(1)
        self.node_pos = [-1 for _ in range(node_num)]  # 下标初始化为-1, 表示尚未加入堆

    def __len__(self):
        return len(self.heap)

    def parent(self, index) -> int:
        '''对应下标的父节点'''
        return (index - 1) // 2

    def left_child(self, index) -> int:
        '''对应下标的左子节点'''
        return 2 * index + 1

    def right_child(self, index) -> int:
        '''对应下标的右子节点'''
        return 2 * index + 2

    def get_min(self) -> (Node | None):
        '''返回最小堆的堆顶元素'''
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, node: Node):
        '''插入节点node到最小堆中'''
        assert self.node_pos[node.node_id] == -1  # 节点之前必须不在堆中
        self.heap.append(node)
        self.node_pos[node.node_id] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def decrease_key(self, node: Node):
        '''更新节点node在堆中的权重'''
        node_id, weight = node.node_id, node.weight
        assert self.node_pos[node.node_id] != -1  # 节点之前必须在堆中
        index = self.node_pos[node_id]  # 找到节点当前在堆中位置
        cur_node = self.heap[index]
        assert isinstance(cur_node, Node) and cur_node.node_id == node_id
        if compare_op(cur_node.weight, weight):
            self.heap[index] = node  # 更新节点权重
            self._heapify_up(index)  # 向上调整堆结构

    def extract_min(self) -> (Node | None):
        '''弹出并返回堆顶元素'''
        if not self.heap:
            return None

        min_node = self.heap[0]
        last_node = self.heap.pop()
        assert isinstance(min_node, Node) and isinstance(last_node, Node)
        if self.heap:
            self.heap[0] = last_node
            self.node_pos[last_node.node_id] = 0
            self._heapify_down(0)
        assert self.node_pos[min_node.node_id] != -1
        self.node_pos[min_node.node_id] = -1  # 删除被弹出节点的位置映射
        return min_node

    def _heapify_up(self, index):
        '''向上调整堆'''
        while index > 0 and \
                compare_op(self.heap[self.parent(index)], self.heap[index]):
            self._swap_node(index, self.parent(index))
            index = self.parent(index)

    def _heapify_down(self, index):
        '''向下调整堆'''
        min_index = index
        left = self.left_child(index)
        if left < len(self.heap) and \
                compare_op(self.heap[min_index], self.heap[left]):
            min_index = left
        right = self.right_child(index)
        if right < len(self.heap) and \
                compare_op(self.heap[min_index], self.heap[right]):
            min_index = right
        if index != min_index:
            self._swap_node(index, min_index)
            self._heapify_down(min_index)

    def _swap_node(self, a_node_index: int, b_node_index: int):
        '''交换堆中的两个节点位置'''
        a_node = self.heap[a_node_index]
        b_node = self.heap[b_node_index]
        assert isinstance(a_node, Node) and isinstance(b_node, Node)
        self.heap[a_node_index] = b_node
        self.heap[b_node_index] = a_node
        # 更新节点及其在数组中对应的下标
        self.node_pos[a_node.node_id] = b_node_index
        self.node_pos[b_node.node_id] = a_node_index


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(Node(5, 1, 5))
    heap.insert(Node(4, 1, 4))
    heap.insert(Node(3, 1, 3))
    heap.insert(Node(2, 1, 2))
    heap.insert(Node(1, 1, 1))
    print(heap.get_min())
    heap.decrease_key(Node(4, 1, 0))
    print(heap.get_min())
    print(heap.heap)
    print(heap.node_pos)
    for i in range(5):
        print(heap.extract_min())
