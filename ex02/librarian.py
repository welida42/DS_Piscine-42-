#!/usr/bin/env python3
import os


def ft_env():
    if os.environ["VIRTUAL_ENV"][-11:] != "ex02/welida":
        raise Exception("incorrect venv")
    with open("requirements.txt", "w") as f:
        f.write("BeautifulSoup4\npytest\n")
    os.system("pip install -r requirements.txt")
    os.system("pip freeze")
    os.system("pip freeze > requirements.txt")


if __name__ == "__main__":
    try:
        ft_env()
    except Exception as e:
        print("Error:", e)
