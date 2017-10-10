DIGITS = "0123456789"


def split(s, n):
    t = s
    while t:
        yield t[:n]
        t = t[n:]


def get_digits(filename):
    with open(filename) as f:
        data = f.read()
    return [ int(c) for c in data if c in DIGITS ]
