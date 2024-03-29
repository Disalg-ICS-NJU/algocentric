# 矩阵连乘

## 问题描述

定n个矩阵：A[1],A[2],...,A[n]，其中A[i]与A[i+1]是可乘的(i=1,2,...,n-1)。

确定计算矩阵连乘积的计算次序，使得依此次序计算矩阵连乘积需要的数乘次数最少。

注意，根据矩阵乘法定义，两个矩阵相乘意味着后一矩阵的行数与前一矩阵的列数相同。

## 输入

两行内容, 第一行为矩阵个数n的值,
第二行为由空格分隔的整数序列, n+1个数依次是n个矩阵的行数以及最后一个矩阵的列数, 
例如:

```txt
5
5 10 4 6 10 2
```

## 输出

计算矩阵连乘积的计算次序和最少数乘次数, 例如:

```txt
(A[0](A[1](A[2](A[3]A[4]))))
348
```
