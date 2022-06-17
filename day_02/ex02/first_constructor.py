import sys


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        with open(self.path, "r") as f:
            lines = f.readlines()
            if len(lines) < 2:
                raise Exception("Incorrect lines count")
            if len(lines[0].split(",")) != 2:
                raise Exception("Incorrect header")
            head = lines[0]
            for i in range(1, len(lines)):
                if len(lines[i].split(",")) != 2:
                    raise Exception("Incorrect columns count")
                splited = lines[i].strip("\n").split(",")
                if (splited[0] != "0" and splited[0] != "1") or (splited[1] != "0" and splited[1] != "1"):
                    raise Exception("Incorrect value")
                if splited[0] == splited[1]:
                    raise Exception("Incorrect value")
                head += lines[i]
            return head


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception("Incorrect arguments count")
        example = Research(sys.argv[1])
        print(example.file_reader())
    except Exception as e:
        print(e)
