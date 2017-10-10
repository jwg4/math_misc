from helpers import split


DIGITS = "0123456789"
FILENAME = "pi.txt"


def get_digits(filename):
    with open(filename) as f:
        data = f.read()
    return [ int(c) for c in data if c in DIGITS ]


def print_digits(l):
    for r in split(l, 30):
        print(make_line(r))


def make_line(l):
    FORMAT = "  ".join(["%d%d%d %d%d%d"] * 5)
    return FORMAT % tuple(l)


if __name__ == '__main__':
    print_digits(get_digits(FILENAME))
