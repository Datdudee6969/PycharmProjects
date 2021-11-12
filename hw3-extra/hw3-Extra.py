# Kyron Claitt
# U74837309

def read():
    file = open('hw3-ExtraCredit.txt', "r")
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values


def list_duplicates():
    seen = set()
    seen_add = seen.add
    seen_twice = set(x for x in read() if x in seen or seen_add(x))
    return list(seen_twice)


print("The Duplicate Numbers: ", list_duplicates())
