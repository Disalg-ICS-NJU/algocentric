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
import argparse


def get_random_input(length: int, random_range: tuple, given_k: int) -> list:
    '''获取随机数list

    Args:
        length (int): 随机数list的长度
        random_range (tuple): 随机数的大小范围
        given_k(tuple): 给定的常数k

    Returns:
        随机数list
    '''
    candidate_list = []
    for _ in range(given_k):
        candidate_list.append(randint(*random_range))
    random_list = []
    for _ in range(length):
        random_list.append(candidate_list[randint(0, given_k-1)])
    return random_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Genrate random test inputs")
    parser.add_argument('-l', dest='min_len', type=int, default=0,
                        help="min list length")
    parser.add_argument('-L', dest='max_len', type=int, default=1000,
                        help="max list length")
    parser.add_argument('-m', dest='min', type=int, default=-5000,
                        help="min random number")
    parser.add_argument('-M', dest='max', type=int, default=5000,
                        help="max random number")
    parser.add_argument('-k', dest='min_k', type=int, default=2,
                        help="min random k")
    parser.add_argument('-K', dest='max_k', type=int, default=20,
                        help="max random k")
    parser.add_argument(dest='num', type=int, default=10, nargs='?',
                        help="number of test input")
    args = parser.parse_args()
    for _ in range(args.num):
        random_length = randint(args.min_len, args.max_len)
        k = randint(args.min_k, args.max_k)
        new_list = get_random_input(random_length, (args.min, args.max), k)
        print(' '.join(map(str, new_list)))
        print(k)
