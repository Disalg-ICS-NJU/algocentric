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


def get_random_input(length: int, random_range: tuple) -> list:
    '''获取随机数list

    Args:
        length (int): 随机数list的长度
        random_range (tuple): 随机数的大小范围

    Returns:
        随机数list
    '''

    random_list = []
    for _ in range(length):
        random_list.append(randint(*random_range))
    return random_list


if __name__ == '__main__':
    length = randint(1, 1000)
    random_range = (-5000, 5000)
    for _ in range(10):
        new_list = get_random_input(length, random_range)
        print(' '.join(map(str, new_list)))
