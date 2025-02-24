#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2025 Ruize Tang <tangruize97@qq.com>, Runze Wu
# <runzewu@smail.nju.edu.cn>, Peiyang He <peiyang_he@smail.nju.edu.cn>
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
import argparse


def get_random_input(num_points: int, x_range: tuple, y_range: tuple) -> list:
    '''获取随机的点集, 保证结果长度大于1且其中没有相同的点

    Args:
        num_points (int): 生成的点的数量
        x_range (tuple): 横坐标的取值范围
        y_range (tuple): 纵坐标的取值范围

    Returns:
        点集
    '''
    random_list = set()
    while len(random_list) < num_points:
        new_point = (randint(*x_range), randint(*y_range))
        random_list.add(new_point)  # 使用 set 自动去重
    return list(random_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate random test inputs")
    parser.add_argument('-n', dest='num_points', type=int, default=10,
                        help="number of points")
    parser.add_argument('-x', dest='min_x', type=int, default=-10000,
                        help="min x value")
    parser.add_argument('-X', dest='max_x', type=int, default=10000,
                        help="max x value")
    parser.add_argument('-y', dest='min_y', type=int, default=-10000,
                        help="min y value")
    parser.add_argument('-Y', dest='max_y', type=int, default=10000,
                        help="max y value")
    parser.add_argument(dest='num', type=int, default=10, nargs='?',
                        help="number of test input")
    args = parser.parse_args()
    if args.num_points < 2:
        parser.error("number of points must be greater than 2")
    if args.min_x > args.max_x:
        parser.error("min_x must be smaller than or equal to max_x")
    if args.min_y > args.max_y:
        parser.error("min_y must be smaller than or equal to max_y")
    if (args.max_x - args.min_x) * (args.max_y - args.min_y) < args.num_points:
        parser.error("cannot generate distinct points of the required number")
    for _ in range(args.num):
        new_list = (
            get_random_input(args.num_points, (args.min_x, args.max_x), (args.min_y, args.max_y)))
        print(args.num_points)
        for point in new_list:
            print(str(point[0]) + " " + str(point[1]))
