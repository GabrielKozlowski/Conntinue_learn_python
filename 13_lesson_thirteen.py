


# class NoDuplicates:

#     def __init__(self):
#         self.list = []
    
#     def __call__(self, new_items):        
#         for item in new_items:
#             if item not in self.list:
#                 self.list.append(item)

# my_no_dup_list = NoDuplicates()
# print(my_no_dup_list.list)
# my_no_dup_list(['keyboard','mouse'])
# print(my_no_dup_list.list)
# my_no_dup_list(['keyboard','mouse','pendrive'])
# my_no_dup_list(['charger','pendrive'])
# print(my_no_dup_list.list)

# # *****************************************************************************************

# class Add_additives:

#     def __init__(self, func):
#         self.func = func

#     def __call__(self, cake, additives):
#         no_duplicate_list = []
#         for additive in additives:
#             if additive not in cake.additives:
#                 no_duplicate_list.append(additive)
#         self.func(cake, no_duplicate_list)        


# class Cake:
#     bakery_offer = []
    
#     def __init__(self, name, kind, taste, additives, filling):
 
#         self.name = name
#         self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
 
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#         print('-'*20)
 
#     def add_additives(self, additives):
#         self.additives.extend(additives)
 
 
# cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

# @Add_additives
# def add_extra_additives(cake, additives):
#     cake.add_additives(additives)


# new_cake = Add_additives(add_extra_additives(cake01,[]))
# print('\n----------Before----------')
# cake01.show_info()
# new_cake = Add_additives(add_extra_additives(cake01,['nuts', 'toffe']))
# print('\n----------After----------')
# cake01.show_info()
# new_cake = Add_additives(add_extra_additives(cake01,['fruits', 'nuts', 'coconut shrims']))
# print('\n----------Last----------')
# cake01.show_info()
# #******************************************************************************




