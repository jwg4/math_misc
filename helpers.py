def split(s, n):
    t = s
    while t:
        yield t[:n]
        t = t[n:]
