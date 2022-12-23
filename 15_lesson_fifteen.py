

# class Cake:

#     """
#     Cake - class operating on cakes available in bakery
#     """
 
#     bakery_offer = []
 
#     def __init__(self, name, kind, taste, additives, filling):
               
#         """
#             init - arguments accepted:
#             name - the name of the cake
#             kind - the kind of the cake
#             taste - the taste of the cake
#             additives - the cake additives
#             filling - the filling of the cake
#             bakery_offer - list of all cakes 
#         """

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
 
#     @property
#     def full_name(self):
#         """ return name upper and kind of cake """
       
#         return "--== {} - {} ==--".format(self.name.upper(), self.kind)

# help(Cake)
# help(Cake.full_name)
# # *******************************************************************************************************************

