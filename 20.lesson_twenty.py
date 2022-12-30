
# import itertools as it
# import math

# notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# for a in it.permutations(notes, 4):
#     print(a)


# print("4-notes melody with not repeat. Can be created {} melodys.".format(int(math.factorial(len(notes)) / math.factorial((len(notes) - 4)))))


# for b in it.product(notes, repeat=4):
#     print(b)

# print("4-notes melody with repeats. Can be created {} melodys.".format(int(math.pow(len(notes), 4))))

# #***********************************************************************************************************

import os
import itertools as it

def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry


listing = scantree('./links_to_check/')


for l in listing:
    print(f"{l} is dir" if l.is_dir() else f"{l} is file")


listing = scantree('./links_to_check/')
listing = sorted(listing, key=lambda e: e.is_dir())


for is_dir, elements in it.groupby(listing, key = lambda e: e.is_dir()):
    print('Is dir ' if is_dir else 'Is file', len(list(elements)))


