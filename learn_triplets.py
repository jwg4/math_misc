import random

from helpers import make_lookup


def check_triplet(number, name):
    guess = input("%s?  " % name)
    if guess != int(number):
        print "No! %s is %s" % (name, number)
        return False
    else:
        print ":)"
        return True


if __name__ == '__main__':
    lookup = make_lookup("triplets.txt")
    success = True
    c = 0
    while success:
        s = random.choice(lookup.keys())
        success = check_triplet(s, lookup[s])
        c = c + 1
    print "Streak of %d correct answers." % (c - 1, )
