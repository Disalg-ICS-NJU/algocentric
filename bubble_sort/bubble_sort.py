def bubble_sort(array: list) -> list:
    '''无优化的的冒泡排序算法.

    Args:
        array (list): 未排序的list

    Returns:
        返回排序后的list
    '''

    new_list = list(array)
    for i in range(len(new_list)-1):
        for j in range(0, len(new_list)-i-1):
            if new_list[j] > new_list[j+1]:
                new_list[j], new_list[j+1] = new_list[j+1], new_list[j]
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
