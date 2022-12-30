
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

# import os
# import itertools as it

# def scantree(path):
#     for entry in os.scandir(path):
#         if entry.is_dir():
#             yield entry
#             yield from scantree(entry.path)
#         else:
#             yield entry


# listing = scantree('./links_to_check/')


# for l in listing:
#     print(f"{l} is dir" if l.is_dir() else f"{l} is file")


# listing = scantree('./links_to_check/')
# listing = sorted(listing, key=lambda e: e.is_dir())


# for is_dir, elements in it.groupby(listing, key = lambda e: e.is_dir()):
#     print('Is dir ' if is_dir else 'Is file', len(list(elements)))

# #***********************************************************************************************************
# import itertools

# def get_factors(x):

#     rel_list = []
#     for i in range(1, x):
#         if x % i == 0:
#             rel_list.append(i)
#     return rel_list


# candidate_list = [x for x in range(1, 10001)]
# filtered_list = list(itertools.filterfalse(lambda x: x != sum(get_factors(x)),candidate_list))


# for p in filtered_list:
#     print(p, get_factors(p))
# #***********************************************************************************************************
# import itertools as it

# def check_if_has_dividers(x):
 
#     for i in range(2, x):
#         if x % i == 0:
#             return True
#     else:
#         return False

# prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
# print(prime_numbers)


# print(prime_numbers[:10])

# # pri = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(1000000)),2,10,2)
# # print(list(pri))

# prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
# print(list(prime_numbers))
