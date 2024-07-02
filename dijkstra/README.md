# 单源最短路 Dijkstra 算法

## 问题描述

给定一个加权有向图和源节点 $s$, 使用 Dijkstra 算法找出 $s$ 到所有节点的最短路.

## 输入

有若干行内容, 第一行为由空格隔开的三个整数, 分别表示图的点数 $n$ 、边数 $m$ 和源节点 $s$.  
接下来有 $m$ 行, 每一行为由空格隔开的三个自然数, 依次表示边的起点, 终点以及边的权重.  
为了便于实现, 图中节点编号取值为 $[0,n)$ , 边的权重非负. 例如:

```txt
4 6 0
0 1 2
1 2 2
1 3 1
0 2 5
2 3 3
0 3 4
```

## 输出

一行 $n$ 个数，第 $i$ 个数表示 $s$ 到 $i$ 的最短路的距离. 若点 $i$ 不可达，输出 2147483647 （即 0x7fffffff）

```txt
0 2 4 3
```

## 对于示例代码的解释

### 辅助方法

`generator.py` 用于随机生成输入数据，其参数及解释如下：
```
usage: generator.py [-h] [-n MIN_NODE] [-N MAX_NODE] [-m MIN] [-M MAX] [--has_negative_edges] [--has_negative_cycle] [num]

Genrate random test inputs

positional arguments:
  num                   number of test input

options:
  -h, --help            show this help message and exit
  -n MIN_NODE           min node number
  -N MAX_NODE           max node number
  -m MIN                min edge number
  -M MAX                max edge number
  --has_negative_edges  Whether the graph can have negative edges
  --has_negative_cycle  Whether the graph can have negative cycles
```


`get_input.py` 用于从 `stdin` 读取输入并格式化为 `dijkstra` 和 `bellman-ford` 接受的形式。

`node.py` 、`min_heap.py` 和 `critical_op.py` 提供了在堆操作时对关键操作（比较操作）的计数。

`bellman-ford.py` 作为检查代码正确性的参考。


### 核心算法

`dijkstra.py` 是不含负权边的带权有向图单源最短路算法的实现。

`dijkstra_with_neg_edge.py` 是对原算法的修改，可以正确处理存在负权边（但不含负权环）的情况。

### 测试工具

`check.py` 用于检查 `dijkstra` 的实现。使用的正确参考是 `bellman-ford` 算法。对于错误的结果，输出第一行是输入数据，之后 `n` 行每行两个数，第 `i` 行的两个数分别是 `dijkstra` 和 `bellman-ford` 算法得出的，从源节点到节点 `i` 的最短路径长度。如需使用 `dijkstra_with_neg_edge.py`，将第 27 行修改为：
```
USE_NEGATIVE_EDGES = True
```

`Makefile` 提供了一键回归测试的快捷指令。可以使用 
```
make run
```
运行 `dijkstra.py`，这个选项需要手动输入符合格式的数据。

使用
```
make test
```
运行 `check.py`，调用你的实现和参考实现比对，同样需要手动输入符合格式的数据。

使用
```
make test_no_input
```
自动生成数据并进行测试。在 `Makefile` 第 14 行中，你可以自行修改为 `generator.py` 输入的参数来获得不同的随机生成的数据。比如可以删去 `--has_negative_edges` 来生成不含负权边的有向图。各个参数的定义见 [`generator.py --help`](#辅助方法)

使用
```
make random_test [NUM=100]
```
来进行随机的若干组测试，可以通过 `NUM=100` 显式地指定随机测试的规模。