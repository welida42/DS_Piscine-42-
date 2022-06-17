import sys


def starter(email):
    with open("employees.tsv", "r") as f:
        lines = f.readlines()
        for line in lines:
            e = line.replace("\n", "").split("\t")
            if e[2] == email:
                print(f"Dear {e[0]}, welcome to our team. We are sure that it will be a pleasure to work with \
you. That’s a precondition for the professionals that our company hires.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        starter(sys.argv[1])

