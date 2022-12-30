

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

# import random

# def random_with_sum(numbers_of_values, asserted_sum):

#     trial = 0
#     numbers = list(range(numbers_of_values))

#     while True:
#         trial += 1

#         for i in range(numbers_of_values):
#             numbers[i] = (random.randint(1, 101))

#         if sum(numbers) == asserted_sum:
#             yield (trial, numbers)
#             trial = 0

# for i in range(10):
#     (number_of_trials, numbers) = next(random_with_sum(3, 100))
#     print(number_of_trials, numbers)
# #*****************************************************************************

# import os 
# import requests

# def gen_get_files(dir):
#     for file in os.listdir(dir):
#         yield os.path.join(dir, file)


# def gen_get_file_lines(filename):
#     with open(filename, 'r') as f:
#         for line in f.readlines():
#             yield line.replace('\n',  '')


# def check_webpage(url):

#     try:
#         response = requests.get(url)
#         return response.status_code == 200
#     except:
#         return False


# try:
#     os.mkdir('./links_to_check')
# except:
#     pass

# with open('./links_to_check/pl.txt', 'w') as f:
#     f.write('http://www.wykop.pl/\n')
#     f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
#     f.write('http://www.demotywatory.pl/\n')

# with open('./links_to_check/com.txt', 'w') as f:
#     f.write('http://www.realpython.com/\n')
#     f.write('http://www.nonexistenturl.com/\n')
#     f.write('http://www.stackoverflow.com/\n')


# for file in gen_get_files('./links_to_check'):
#     for line in gen_get_file_lines(file):
#         print("{} - {} - {}".format(file, line, check_webpage(line)))
        
# #*****************************************************************************


