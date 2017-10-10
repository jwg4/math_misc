from helpers import split


def make_lookup(filename):
    d = {}
    with open(filename) as f:
        for line in readlines(f):
            m = re.match("^(\d\d\d)   (.*)$", line)
            if not m:
                raise Exception("The line %s couldn't be parsed properly." % (line, ))
            d[m.group(1)] = m.group(2)
    return d


def _make_hints_text(digits, lookup):
    c = 0
    for triplet in split(digits, 3):
        s = "".join(str(d) for d in triplet)
        hint = lookup[s]
        line = "%s - %s" % (s, hint)
        yield line

        c = c + 1
        if not c % 2:
            yield ""
    yield ""
         
def make_hints_text(digits, lookup):
    print list(_make_hints_text(digits, lookup))
    return "\n".join(_make_hints_text(digits, lookup))        
