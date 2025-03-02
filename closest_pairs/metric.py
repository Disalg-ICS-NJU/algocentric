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

import os
import subprocess
import sys
from typing import List
from matplotlib import pyplot as plt
from closest_pairs import Point, brute_force, divide_and_conquer, closest_pairs, \
    DistanceOP  # pylint: disable=wrong-import-position, no-name-in-module # noqa
from get_input import get_input  # pylint: disable=wrong-import-position, no-name-in-module # noqa


def generate_and_get_input(num: int) -> List[Point]:
    tmp_file = "tmp"
    # 重定向标准输出到临时文件
    with open(tmp_file, "w") as f:
        subprocess.run(["python3", "generator.py", "-n", str(num)], stdout=f, text=True)
    with open(tmp_file, "r") as f:
        sys.stdin = f
        res = get_input()
    os.remove(tmp_file)
    return res


if __name__ == '__main__':
    n_to_test = [10, 20, 50, 100, 150]
    results = {"brute_force": [], "yours": [], "divide_and_conquer": []}
    for n in n_to_test:
        x = generate_and_get_input(n)
        results["brute_force"].append(brute_force(x, DistanceOP())[1])
        results["yours"].append(closest_pairs(x)[1])
        results["divide_and_conquer"].append(divide_and_conquer(x)[1])

    # 折线图
    plt.figure(figsize=(10, 9))
    for algo, color in zip(results.keys(), ['b', 'r', 'g']):
        plt.plot(n_to_test, results[algo], marker='o', label=algo, color=color)
        for i, txt in enumerate(results[algo]):
            plt.text(n_to_test[i], results[algo][i], str(txt), ha='right', va='bottom')

    plt.xlabel("Number of points")
    plt.ylabel("Critical operation count")
    plt.xticks(n_to_test)  # 只显示 n_to_test 作为横坐标刻度
    plt.yscale('log')  # 使用对数尺度, 避免左下方点重合
    plt.legend()
    plt.grid(True)
    plt.show()
