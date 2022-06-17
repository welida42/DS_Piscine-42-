class Must_read:
    try:
        with open("data.csv", "r") as f:
            readed = f.read()
            print(readed)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    Must_read()
