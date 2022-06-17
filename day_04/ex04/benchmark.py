#!/usr/bin/env python3
import timeit
import random
from collections import Counter


def create_dict(lst):
    res = {}
    for i in lst:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res


def top_10(lst):
    return dict(sorted(create_dict(lst).items(), key=lambda item: item[1], reverse=True)[:10])


def main():
    random_list = [random.randint(0, 100) for i in range(1_000_000)]

    my_create_dict = timeit.timeit(lambda: create_dict(random_list), number=1)
    my_top_10 = timeit.timeit(lambda: top_10(random_list), number=1)
    ft_counter = timeit.timeit(lambda: Counter(random_list), number=1)
    ft_counter_top_10 = timeit.timeit(lambda: dict(Counter(random_list).most_common(10)), number=1)
    print("my function:", my_create_dict)
    print("Counter:", ft_counter)
    print("my top:", my_top_10)
    print("Counters top:", ft_counter_top_10)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
