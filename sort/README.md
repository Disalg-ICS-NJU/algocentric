# 排序算法

## 算法描述

本模块中实现了两类经典排序算法:

1. [冒泡排序](./bubble_sort/)
2. [归并排序](./merge_sort/)

以及基于排序算法实现特定需求:

1. [逆序对计数](./counting_inversion/): 基于归并排序.

## 测试

[check.py](./check.py)脚本测试算法结果的正确性, 检查序列是否有序, 或检查逆序对计数是否正确.  
[generator.py](./generator.py)脚本产生多个随机输入序列.  
[Makefile](./Makefile)中定义了若干命令, 便于快速运行和测试算法.  
`make run`进行算法运行, 可以使用`TARGET`指定运行的算法, 例如`make run TARGET=merge_sort`.  
`make test`则对指定算法进行测试.
`make test_no_input`和`make random_test`命令来测试随机输入是否能通过验证.

## 性能分析

排序算法中比较两元素大小是其关键操作, 通过统计比较操作次数可以对排序算法的性能有直观的了解.  
[check.py](./check.py)脚本在测试通过后会输出比较操作次数.
