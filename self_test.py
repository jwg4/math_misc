import sys

from helpers import DIGITS, get_digits


def get_input():
    s = sys.stdin.read()
    return [ int(c) for c in s if c in DIGITS ]


def compare_input(user, real):
    c = 0
    for a, b in zip(user, real):
        if a != b:
            raise Exception("Incorrect digit %d: entered %d, should be %d"
                % (c, a, b)
            )
        c = c + 1
    return c


if __name__ == '__main__':
    r = compare_input(get_input(), get_digits("pi.txt"))
    print "Correctly remembered %d digits." % (r, )
