#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Ruize Tang <tangruize97@qq.com>, Runze Wu
# <runzewu@smail.nju.edu.cn>, Anpu Lu <anpulu@smail.nju.edu.cn>.
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


def get_random_input(n: int, random_range: tuple) -> list:
    '''获取随机数list

    Args:
        n (int): 矩阵个数
        random_range (tuple): 随机数的大小范围

    Returns:
        随机数n和随机数list
    '''
    random_list = []
    for _ in range(n+1):
        random_list.append(randint(*random_range))
    return random_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Genrate random test inputs")
    parser.add_argument('-m', dest='min', type=int, default=1,
                        help="min random number")
    parser.add_argument('-M', dest='max', type=int, default=5000,
                        help="max random number")
    parser.add_argument('-n', dest='min_n', type=int, default=2,
                        help="min random n")
    parser.add_argument('-N', dest='max_n', type=int, default=20,
                        help="max random n")
    parser.add_argument(dest='num', type=int, default=10, nargs='?',
                        help="number of test input")
    args = parser.parse_args()
    for _ in range(args.num):
        n = randint(args.min_n, args.max_n)
        new_list = get_random_input(n, (args.min, args.max))
        print(n)
        print(' '.join(map(str, new_list)))
