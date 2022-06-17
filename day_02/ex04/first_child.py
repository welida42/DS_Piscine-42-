import sys
from random import randint


class Research:
    def __init__(self, path):
        self.path = path
        self.calc = self.Calculations(self.file_reader())

    def file_reader(self, has_header=True):
        with open(self.path, "r") as f:
            lines = f.readlines()
            if has_header is True:
                if len(lines) < 2:
                    raise Exception("Incorrect lines count")
                if len(lines[0].split(",")) != 2:
                    raise Exception("Incorrect header")
                res = []
                for i in range(1, len(lines)):
                    if len(lines[i].split(",")) != 2:
                        raise Exception("Incorrect columns count")
                    splited = lines[i].strip("\n").split(",")
                    if (splited[0] != "0" and splited[0] != "1") or (splited[1] != "0" and splited[1] != "1"):
                        raise Exception("Incorrect value")
                    if splited[0] == splited[1]:
                        raise Exception("Incorrect value")
                    res.append([int(splited[0]), int(splited[1])])
                return res
            else:
                if len(lines) < 1:
                    raise Exception("Incorrect lines count")
                res = []
                for i in range(len(lines)):
                    if len(lines[i].split(",")) != 2:
                        raise Exception("Incorrect columns count")
                    splited = lines[i].strip("\n").split(",")
                    if (splited[0] != "0" and splited[0] != "1") or (splited[1] != "0" and splited[1] != "1"):
                        raise Exception("Incorrect value")
                    if splited[0] == splited[1]:
                        raise Exception("Incorrect value")
                    res.append([int(splited[0]), int(splited[1])])
                return res

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(i[0] for i in self.data)
            tails = sum(i[1] for i in self.data)
            return heads, tails

        def fractions(self, heads_count, tails_count):
            return heads_count / (heads_count + tails_count) * 100, tails_count / (heads_count + tails_count) * 100

class Analitics(Research.Calculations):
    def predict_random(self,  number_of_predictions):
        predictions = []
        for i in range(number_of_predictions):
            if randint(0, 1) == 0:
                predictions.append([0, 1])
            else:
                predictions.append([1, 0])
        return predictions

    def predict_last(self):
        return self.data[-1]

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception("Incorrect arguments count")
        example = Research(sys.argv[1])
        data = example.file_reader()
        print(data)
        head_count, tail_count = example.calc.counts()
        print(head_count, tail_count)
        head_frac, tail_count_frac = example.calc.fractions(head_count, tail_count)
        print(head_frac, tail_count_frac)
        predicts = Analitics(data)
        prediction = predicts.predict_random(3)
        print(prediction)
        last = predicts.predict_last()
        print(last)
    except Exception as e:
        print(e)
