# # Taking dictionary to def .
# cake_01 = {
#         'taste' : 'vanilia',
#         'glaze' : 'chocolade',
#         'text' : 'Happy Brithday',
#         'weight' : 0.7
# }

# cake_02 = {
#         'taste' : 'tee',
#         'glaze' : 'lemon',
#         'text' : 'Happy Python Coding',
#         'weight' : 1.3
# }
 

# def show_cake_info(aCake):
#     print('{} cake with {} glaze with text "{}" of {} kg'.format(
#         aCake['taste'], aCake['glaze'], aCake['text'], aCake['weight']))
 
# show_cake_info(cake_01)
# show_cake_info(cake_02)

# cakes = [cake_01,cake_02]

# for c in cakes:
#     show_cake_info(c)

# #******************************************************************************

# # Create a class for task.


class Cake:

    def __init__(self, name, kind, taste, additves, filling) -> None:
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additves = additves
        self.filling = filling


cake_1 = Cake('Apple_pie', 'cake with apples', 'apple', ['castor sugar'], [])
cake_2 = Cake('Pickaninny_pie', 'black cake', 'cacao', ['icing'], ['chocolade'])


print(cake_1.name, cake_1.kind, cake_1.taste, cake_1.additves, cake_1.filling)
print("My favorite cake is {}, it looks like {} and have taste {}. On top it haves {}.{} ".format(cake_2.name, cake_2.kind, cake_2.taste, cake_2.additves, cake_2.filling))



bakery_offer = [cake_1,cake_2]

for c in bakery_offer:
    print("Today in our offer:\n{} - ({}) main taste: {} with additives of\n{}, filled with {}.\n".format(c.name, c.kind, c.taste, c.additves, c.filling))

