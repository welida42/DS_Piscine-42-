import sys


def extract(name):
    head = "Name\tSurname\tE-mail\n"
    with open(name, "r") as f:
        lines = f.readlines()
        string = ""
        for line in lines:
            splitted = line.split("@")[0].split(".")
            string = string + splitted[0].capitalize() + "\t" + splitted[1].capitalize() + "\t" + line
        head += string
    with open("employees.tsv", "w") as f:
        f.write(head)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        extract(sys.argv[1])
