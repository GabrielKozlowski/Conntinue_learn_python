


# class Combinations:

#     def __init__(self, products, promotions, customers):
#         self.products = products
#         self.promotions = promotions
#         self.customers = customers
        

    
#     def __getitem__(self, item):

       
#         if item >= len(self.products) * len(self.promotions) * len(self.customers):
#             raise StopIteration
#         else:
#             pos_products = item // (len(self.promotions) * len(self.customers))
#             item = item % (len(self.promotions) * len(self.customers))

#             pos_promotions = item // len(self.customers)
#             item = item % len(self.customers)

#             pos_customers = item

#         return "{} - {} - {}".format(self.products[pos_products], self.promotions[pos_promotions], self.customers[pos_customers])



# products = ["Product {}".format(i) for i in range(1, 4)]
# # print(products)
 
# promotions = ["Promotion {}".format(i) for i in range(1, 3)]
# # print(promotions)
 
# customers = ['Customer {}'.format(i) for i in range(1, 6)]
# # print(customers)
 
# combinations = Combinations(products, promotions, customers)


# # for i in range(0, 31):
# #     print(i, combinations[i])

# combinations_iterator = iter(combinations)
# print(next(combinations_iterator))


# for c in combinations_iterator:
#     print(c)
 
# #****************************************************************************

# import csv
 
# with open('./csv.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     # for row in csvreader:
#     #     print('|'.join(row))
#     while True:
#         try:
#             print(next(csvreader))
#         except StopIteration:
#             break

# #****************************************************************************


# class CombinationsIterator:

#     def __init__(self, products, promotions, customers):
#         self.products = products
#         self.promotions = promotions
#         self.customers = customers
 
#         self.current_product = 0
#         self.current_promotion = 0
#         self.current_customer = 0


#     def __next__(self):
 
#         if self.current_customer >= len(self.customers):
#             self.current_customer = 0
#             self.current_promotion += 1
 
#         if self.current_promotion >= len(self.promotions):
#             self.current_promotion = 0
#             self.current_product += 1
 
#         if self.current_product >= len(self.products):
#             self.current_product =0
#             raise StopIteration()
 
#         item_to_return = "{} - {} -{}".format(self.products[self.current_product],
#                                               self.promotions[self.current_promotion],
#                                               self.customers[self.current_customer])
 
#         self.current_customer += 1
 
#         return  item_to_return
 

# class Combinations:
 
#     def __init__(self, products, promotions, customers):
#         self.products = products
#         self.promotions = promotions
#         self.customers = customers
 
#         self.iteratior = CombinationsIterator(self.products, self.promotions, self.customers)
 
    
#     def __iter__(self):
#         return  self.iteratior
 
 
# products = ["Product {}".format(i) for i in range(1, 4)]
# promotions = ["Promotion {}".format(i) for i in range(1, 3)]
# customers = ['Customer {}'.format(i) for i in range(1, 5)]
 
# combinations = Combinations(products, promotions, customers)
 
# for c in combinations:
#     print(c)

# #****************************************************************************


