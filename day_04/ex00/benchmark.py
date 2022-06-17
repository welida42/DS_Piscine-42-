#!/usr/bin/env python3
import timeit


def ft_loop(emails):
    res = []
    for i in emails:
        if i.endswith("@gmail.com"):
            res.append(i)
    return res


def ft_list_comprehension(emails):
    return [i for i in emails if i.endswith("@gmail.com")]


def main():
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    count = 90_000
    loop = timeit.timeit(lambda: ft_loop(emails), number=count)
    lc = timeit.timeit(lambda: ft_list_comprehension(emails), number=count)
    if loop > lc:
        print(f"it is better to use a list comprehension\n{lc} vs {loop}")
    else:
        print(f"it is better to use a loop\n{lc} vs {loop}")


if __name__ == "__main__":
    main()
