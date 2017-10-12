import re

from helpers import split, get_digits


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


def _make_hints_text(digits, lookup):
    c = 0
    for triplet in split(digits, 3):
        s = "".join(str(d) for d in triplet)
        try:
            hint = lookup[s]
        except:
            raise Exception("We don't have a hint for %s." % (s, ))
        line = "%s - %s" % (s, hint)
        yield line

        c = c + 1
        if not c % 2:
            yield ""
        if not c % 10:
            yield "---"
            yield ""
    yield ""
         

def make_hints_text(digits, lookup):
    return "\n".join(_make_hints_text(digits, lookup))        


if __name__ == '__main__':
    digits = get_digits("pi.txt")
    digits = digits[:60]
    lookup = make_lookup("triplets.txt")
    print make_hints_text(digits, lookup)   
