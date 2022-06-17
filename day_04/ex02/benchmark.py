#!/usr/bin/env python3
import timeit
import sys


def ft_loop(emails):
    res = []
    for i in emails:
        if i.endswith("@gmail.com"):
            res.append(i)
    return res


def ft_list_comprehension(emails):
    return [i for i in emails if i.endswith("@gmail.com")]


def ft_map(emails):
    return list(map(lambda i: i if i.endswith("@gmail.com") else None, emails))
    #return map(lambda i: i if i.endswith("@gmail.com") else None, emails)


def ft_filter(emails):
    return list(filter(lambda i: i.endswith("@gmail.com"), emails))


def main():
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    ft_dict = {"loop": ft_loop, "list_comprehension": ft_list_comprehension, "map": ft_map, "filter": ft_filter}

    if sys.argv[1] in ft_dict:
        ft_name = sys.argv[1]
    else:
        raise Exception("incorrect argument")
    if sys.argv[2].isdigit():
        count = int(sys.argv[2])
    else:
        raise Exception("incorrect argument")

    print(timeit.timeit(lambda: ft_dict[ft_name](emails), number=count))


if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            raise Exception("incorrect arguments count")
        main()
    except Exception as e:
        print("Error:", e)
