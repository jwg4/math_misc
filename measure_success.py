import re


def generate_success_record(filename):
    with open(filename) as infile:
        for line in infile.readlines():
            m = re.match(".* --- ([0-9]+)$", line)
            yield int(m.group(1))

            
def get_success_record(filename):
    successes = list(generate_success_record(filename))
    successes.sort()
    return successes[-3]


if __name__ == '__main__':
    s = get_success_record("success_log.txt")
    print s
