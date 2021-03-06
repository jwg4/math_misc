import re

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


def make_lookup(filename):
    d = {}
    with open(filename) as f:
        for line in f.readlines():
            m = re.match("^(\d\d\d)(   (.*))?$", line)
            if not m:
                raise Exception("The line %s couldn't be parsed properly." % (line, ))
            if m.group(2):
                d[m.group(1)] = m.group(3)
    return d


def get_try_number(filename):
    s = get_success_number(filename)
    return (s / 30 + 1) * 30


def get_success_number(filename):
    with open(filename, "r") as infile:
        s = infile.read()
        s.strip()
        return int(s)
