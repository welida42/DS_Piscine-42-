def data_types():
    data = [type(1), type("a"), type(1.1), type(True), type([1]), type({1: 2}), type((1, 2)), type({3})]

    res=[]
    for i in data:
        res.append(i.__name__)
    print('[', end="")
    print(*res, end="", sep=", ")
    print(']')


if __name__ == '__main__':
    data_types()
