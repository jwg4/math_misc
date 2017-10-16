import random

from helpers import make_lookup


def check_triplet(number, name):
    name = lookup[number]
    guess = input("%s?  " % name)
    actual = lookup[str(guess)]
    if guess != int(number):
        print "No! %s is %s" % (name, number)
        print "(%s is %s)" % (guess, actual)
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
        success = check_triplet(s, lookup)
        c = c + 1
    print "Streak of %d correct answers." % (c - 1, )
