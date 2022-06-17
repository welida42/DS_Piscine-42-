import sys


def get_price(name):
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    name = name.replace(" ", "") # name =
    if name.find(",,") >= 0:
        return
    name = name.split(",")
    for i in name:
        finded = False
        for key, value in COMPANIES.items():
            if key.lower() == i.lower():
                print(f"{key} stock price is {STOCKS[value]}")
                finded = True
                break
            elif value.lower() == i.lower():
                print(f"{value} is a ticker symbol for {key}")
                finded = True
                break
        if finded == False:
            print(i, "is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_price(sys.argv[1])