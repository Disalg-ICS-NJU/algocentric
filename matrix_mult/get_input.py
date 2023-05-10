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

def get_input() -> (int, list):
    '''从标准输入获取输入, 共两行内容, 第一行为n值, 第二行为由空格分隔的整数序列

    Returns:
        返回n值和整数序列
    '''
    n = int(input())
    array = list(map(int, input().split()))
    return n, array
