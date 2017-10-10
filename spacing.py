from helpers import split, get_digits

FILENAME = "pi.txt"


def print_digits(l):
    for r in split(l, 30):
        print(make_line(r))


def make_line(l):
    FORMAT = "  ".join(["%d%d%d %d%d%d"] * 5)
    return FORMAT % tuple(l)


if __name__ == '__main__':
    print_digits(get_digits(FILENAME))
