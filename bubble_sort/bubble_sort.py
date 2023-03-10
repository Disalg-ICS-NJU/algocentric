CRITICAL_OP_COUNTS = 0


def compare(a: int, b: int) -> bool:
    """排序算法中的比较操作

    Args:
        a (int): 待比较元素a
        b (int): 待比较元素b

    Returns:
        bool: 若a大于b则返回True, 否则为False
    """
    global CRITICAL_OP_COUNTS
    CRITICAL_OP_COUNTS += 1
    return a > b


def bubble_sort(array: list, optimize=False) -> list:
    '''冒泡排序算法.

    Args:
        array (list): 未排序的list
        optimize (bool, optional): 是否为优化冒泡排序算法. 默认为无优化版本

    Returns:
        返回排序后的list
    '''

    new_list = list(array)
    for i in range(len(new_list)-1):
        flag = False
        for j in range(0, len(new_list)-i-1):
            if compare(new_list[j], new_list[j+1]):
                flag = True
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
        if optimize and flag == False:
            break
    return new_list


def get_input() -> list:
    '''从标准输入获取待排序的list, 输入为一行由空格隔开的待排序整数

    Returns:
        待排序的list
    '''

    return list(map(lambda x: int(x), input().split()))


if __name__ == '__main__':
    testcase = get_input()
    result = bubble_sort(testcase)
    print(' '.join(map(lambda x: str(x), result)))