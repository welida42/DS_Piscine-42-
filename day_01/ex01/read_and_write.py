def read_write():
    arr = ""
    with open("ds.csv") as f:
        lines = f.readlines()
        for line in lines:
            splited = line.replace('",', '"\t').replace(',"', '\t"').split("\t")
            res = splited[0:3]
            res.append(splited[3].replace(",", "\t"))
            res.append(splited[4])
            arr = arr + "\t".join(res)
    with open("ds.tsv", "w") as f:
        f.write(arr)


if __name__ == '__main__':
    read_write()
