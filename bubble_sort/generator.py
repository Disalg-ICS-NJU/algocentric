from random import randint


def get_random_input(length: int, ramdom_range: tuple) -> list:
    '''获取随机数list

    Args:
        length (int): 随机数list的长度
        ramdom_range (tuple): 随机数的大小范围

    Returns:
        随机数list
    '''

    ramdom_list = []
    for _ in range(length):
        ramdom_list.append(randint(*ramdom_range))
    return ramdom_list


if __name__ == '__main__':
    length = randint(1, 1000)
    ramdom_range = (-5000, 5000)
    for _ in range(10):
        new_list = get_random_input(length, ramdom_range)
        print(' '.join(map(lambda x: str(x), new_list)))
