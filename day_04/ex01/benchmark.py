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


def ft_map(emails):
    return list(map(lambda i: i if i.endswith("@gmail.com") else None, emails))
    #return map(lambda i: i if i.endswith("@gmail.com") else None, emails)


def main():
    emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
    count = 90_000
    loop = timeit.timeit(lambda: ft_loop(emails), number=count)
    lc = timeit.timeit(lambda: ft_list_comprehension(emails), number=count)
    ma = timeit.timeit(lambda: ft_map(emails), number=count)
    res_dict = {"loop": loop, "list comprehension": lc, "map": ma}
    res_dict = sorted(res_dict.items(), key=lambda item: item[1])
    print(f"it is better to use a {res_dict[0][0]}\n{res_dict[0][1]} vs {res_dict[1][1]} vs {res_dict[2][1]}")


if __name__ == "__main__":
    main()
