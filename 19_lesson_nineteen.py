def combinations(products, promotions, customers):

    for p in products:
        for l in promotions:
            for c in customers:
                yield(p,l,c)

    
products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]
 
for c in combinations(products, promotions, customers):
    print(c)

