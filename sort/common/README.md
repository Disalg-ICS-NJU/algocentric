# 常用的函数

此目录的python文件包含了一些可复用的函数:

- get_input(): 从标准输入获取待排序的list
- compare_op: 用于提供元素比较接口并维护比较操作的次数

可通过下面的语句将它们import:

```python
import sys
import os
# 将sort目录放入python搜索路径中, 使得下面的 from common import ... 能成功执行.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common import get_input, compare_op  # noqa
```
