class Research:
    def file_reader(self):
        with open("data.csv", "r") as f:
            readed = f.read()
            return readed


if __name__ == "__main__":
    try:
        print(Research().file_reader())
    except Exception as e:
        print(e)
