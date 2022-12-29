

# def combinations(products, promotions, customers):

#     for p in products:
#         for l in promotions:
#             for c in customers:
#                 yield(p,l,c)

    
# products = ["Product {}".format(i) for i in range(1, 4)]
# promotions = ["Promotion {}".format(i) for i in range(1, 2)]
# customers = ['Customer {}'.format(i) for i in range(1, 5)]
 
# for c in combinations(products, promotions, customers):
#     print(c)

# #*****************************************************************************

import random

def random_with_sum(numbers_of_values, asserted_sum):

    trial = 0
    numbers = list(range(numbers_of_values))

    while True:
        trial += 1

        for i in range(numbers_of_values):
            numbers[i] = (random.randint(1, 101))

        if sum(numbers) == asserted_sum:
            yield (trial, numbers)
            trial = 0

for i in range(10):
    (number_of_trials, numbers) = next(random_with_sum(3, 100))
    print(number_of_trials, numbers)
# #*****************************************************************************



