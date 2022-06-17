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

    for key, value in COMPANIES.items():
        if key.lower() == name:
            print(STOCKS[value])
            return
    print("Unknown company")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_price(sys.argv[1].lower())

