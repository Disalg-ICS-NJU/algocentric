import bubble_sort


def check(oracle, to_check) -> bool:
    '''检查oracle和to_check是否完全一致.

    Args:
        oracle: 给定的正确结果
        to_check: 待验证的输入

    Returns:
        oracle是否与to_check完全一致的检查结果
    '''
    return oracle == to_check


def sort_check(array: list, to_check: list) -> bool:
    '''检查给定to_check是否为array排序后的结果.

    Args:
        array (list): 未排序的原始输入list
        to_check (list): 待检查的list

    Returns:
        to_check是否为array排序后的结果
    '''
    oracle = sorted(list(array))
    return check(oracle, to_check)


if __name__ == '__main__':
    testcase = bubble_sort.get_input()
    result = bubble_sort.bubble_sort(testcase)
    if sort_check(testcase, result):
        print('PASS')
    else:
        print('FAIL')
        print('Input :', testcase)
        print('Result:', result)
        exit(1)
