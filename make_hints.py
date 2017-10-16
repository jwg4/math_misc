from helpers import split, get_digits, make_lookup, get_try_number


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
    n = get_try_number("success_number")
    digits = digits[:n]
    lookup = make_lookup("triplets.txt")
    print make_hints_text(digits, lookup)   
