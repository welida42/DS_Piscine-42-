#!/usr/bin/env python3
import timeit
import sys
from functools import reduce

def ft_loop(n):
    res = 0
    for i in range(n + 1):
        res += i ** 2
    return res


def ft_reduce(n):
    return reduce((lambda res, i: res + i ** 2), range(n + 1))


def main():
    ft_dict = {"loop": ft_loop, "reduce": ft_reduce}

    if sys.argv[1] in ft_dict:
        ft_name = sys.argv[1]
    else:
        raise Exception("incorrect argument")
    if sys.argv[2].isdigit() and sys.argv[3].isdigit():
        count = int(sys.argv[2])
        n = int(sys.argv[3])
    else:
        raise Exception("incorrect argument")

    print(timeit.timeit(lambda: ft_dict[ft_name](n), number=count))


if __name__ == "__main__":
    try:
        if len(sys.argv) != 4:
            raise Exception("incorrect arguments count")
        main()
    except Exception as e:
        print("Error:", e)
