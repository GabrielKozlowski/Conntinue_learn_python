# import pickle
# import glob

# class Cake:

#     known_kinds = ['cake', 'waffle', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
#     bakery_offer = []

#     def __init__(self, name, kind, taste, additives, filling, gluten_free, text) -> None:
#         self.name = name
#         if kind in self.known_kinds:
#             self.kind = "other" 
#         else:
#             self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.__gluten_free = gluten_free
#         if kind == 'cake with apples' or text == '':
#             self.__text = text
#         else:
#             self.__text = ''
            
#         Cake.bakery_offer.append(self)

#     def show_info(self):
#         print('{}'.format(self.name).upper())
#         print('Kind: {}'.format(self.kind))
#         print('Taste: {}'.format(self.taste))
#         if len(self.additives) > 0:
#             print('additives:')
#             for additive in self.additives:
#                 print('\t{}'.format(additive))
#         if len(self.filling) > 0:
#             print('Filling: \n\t{}'.format(self.filling))
#         else:
#             print('Filling: ')
#         print('Glutten free: {}'.format(self.__gluten_free)) 
#         if len(self.__text) > 0:
#             print('Text on: "{}" is: \n[{}]'.format(self.kind, self.__text))


#     def set_filling(self, filling):
#         self.filling = filling

#     def add_additives(self, additives):
#         self.additives.extend(additives) 

#     def __get_text(self):
#         return self.__text
    
#     def __set_text(self, new_text):
#         if self.kind == 'cake with apples':
#             self.__text = new_text
#         else:
#             print('>>>>>Text can be set only for cake with apples ({})<<<<<'.format(self.name))
    
#     Text = property(__get_text, __set_text, None, 'Text changed')


#     def save_to_file(self,path):
#         with open(path, 'wb') as f:
#             pickle.dump(self,f)

#     @classmethod
#     def read_from_file(cls,path):
#         with open(path, 'rb') as f:
#             newObject = pickle.load(f)
#             cls.bakery_offer.append(newObject)
#             return newObject

#     @staticmethod
#     def get_bakery_file(catalogName):
#         return glob.glob(catalogName + '*.bakery')
        

# cake_1 = Cake('Apple_pie', 'cake with apples', 'apple', ['castor sugar'], '', False, 'Love you')
# cake_2 = Cake('Pickaninny_pie', 'black cake', 'cacao', ['icing', 'nuts'], 'chocolade', False, '')
# cake_3 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
# cake_4 = Cake('Cocoa waffle','waffle','cocoa', [],'cocoa', False, '')

# cake_1.save_to_file('./cake1.bakery')
# cake_2.save_to_file('./cake2.bakery')

# print('-'* 50)
# print('Today in our offer:\n')
# for c in Cake.bakery_offer:
#     Cake.show_info(c)
#     print()

# print('-+'* 50)
# cake_5 = Cake.read_from_file('./cake1.bakery')
# Cake.show_info(cake_5)

# print()
# print(Cake.get_bakery_file('./'))

# # ********************************************************************************

# class Cake:
 
#     known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
#     bakery_offer = []
    
#     def __init__(self, name, kind, taste, additives, filling, gluten_free,text):
 
#         self.name = name
#         if kind in self.known_kinds:
#             self.kind = kind
#         else:
#             self.kind = 'other'
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
#         self.__gluten_free = gluten_free
#         if kind == 'cake' or text == '':
#             self.__text = text
#         else:
#             self.__text = ''
#             print('>>>>>Text can be set only for cake ({})'.format(name))
 
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
#         print("Gluten free: {}".format(self.__gluten_free))
#         if len(self.__text) > 0:
#             print("Text:      {}".format(self.__text))
#         print('-'*20)
 
#     def set_filling(self, filling):
#         self.filling = filling
 
#     def add_additives(self, additives):
#         self.additives.extend(additives)

#     @property
#     def Text(self):
#         return self.__text

#     @Text.setter
#     def Text(self, new_text):
#         if self.kind == 'cake':
#             self.__text = new_text
#         else:
#             print('>>>>>Text can be set only for cake ({})'.format(self.name))
    
#     @Text.deleter
#     def Text(self):
#         self.__text = None

# cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
# cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
# cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
# cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')
 
# print("Today in our offer:")
# for c in Cake.bakery_offer:
#     c.show_info()
 
# cake01.Text = 'Happy birthday!'
# cake02.Text = '18'


# for c in Cake.bakery_offer:
#     c.show_info()


# print(cake01.Text)
# cake01.Text = 'Happy death'
# print(cake01.Text)
# del cake01.Text
# print(cake01.Text)

# #*******************************************************************************************
# import types

# def export_1_cake_to_html(obj, path):
#     template = """
# <table border=1>
#      <tr>
#        <th colspan=2>{}</th>
#      </tr>
#        <tr>
#          <td>Kind</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Taste</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Additives</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Filling</td>
#          <td>{}</td>
#        </tr>
# </table>"""
    

#     with open(path, "w") as f:
#         content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
#         f.write(content)


# def export_all_cakes_to_html(cls, path):
#     template_header = """
# <table border=1>"""
#     template = """
#      <tr>
#        <th colspan=2>{}</th>
#      </tr>
#        <tr>
#          <td>Kind</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Taste</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Additives</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Filling</td>
#          <td>{}</td>
#        </tr>"""
#     template_footer = """
# </table>"""
    

#     with open(path, "w") as f:
#         f.write(template_header)
#         for cake in cls.bakery_offer:
#             content = template.format(cake.name, cake.kind, cake.taste, cake.additives, cake.filling)
#             f.write(content)
#         f.write(template_footer)


# def export_this_cake_to_html(self, path):
#     template = """
# <table border=1>
#      <tr>
#        <th colspan=2>{}</th>
#      </tr>
#        <tr>
#          <td>Kind</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Taste</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Additives</td>
#          <td>{}</td>
#        </tr>
#        <tr>
#          <td>Filling</td>
#          <td>{}</td>
#        </tr>
# </table>"""
    

#     with open(path, "w") as f:
#         content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
#         f.write(content)






# class Cake:

#     known_kinds = ['cake', 'waffle', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
#     bakery_offer = []

#     def __init__(self, name, kind, taste, additives, filling, gluten_free, text) -> None:
#         self.name = name
#         if kind in self.known_kinds:
#             self.kind = "other" 
#         else:
#             self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.__gluten_free = gluten_free
#         if kind == 'cake with apples' or text == '':
#             self.__text = text
#         else:
#             self.__text = ''
            
#         self.bakery_offer.append(self)

#     def show_info(self):
#         print('{}'.format(self.name).upper())
#         print('Kind: {}'.format(self.kind))
#         print('Taste: {}'.format(self.taste))
#         if len(self.additives) > 0:
#             print('additives:')
#             for additive in self.additives:
#                 print('\t{}'.format(additive))
#         if len(self.filling) > 0:
#             print('Filling: \n\t{}'.format(self.filling))
#         else:
#             print('Filling: ')
#         print('Glutten free: {}'.format(self.__gluten_free)) 
#         if len(self.__text) > 0:
#             print('Text on: "{}" is: \n[{}]'.format(self.kind, self.__text))


#     def set_filling(self, filling):
#         self.filling = filling

#     def add_additives(self, additives):
#         self.additives.extend(additives) 

#     def __get_text(self):
#         return self.__text
    
#     def __set_text(self, new_text):
#         if self.kind == 'cake with apples':
#             self.__text = new_text
#         else:
#             print('>>>>>Text can be set only for cake with apples ({})<<<<<'.format(self.name))
    
#     Text = property(__get_text, __set_text, None, 'Text changed')


# cake_1 = Cake('Apple pie', 'cake with apples', 'apple', ['castor sugar'], '', False, 'Love you')
# cake_2 = Cake('Pickaninny pie', 'black cake', 'cacao', ['icing', 'nuts'], 'chocolade', False, '')
# cake_3 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
# cake_4 = Cake('Cocoa waffle','waffle','cocoa', [],'cocoa', False, '')


# Cake.export_1_cake_to_html = export_1_cake_to_html
# Cake.export_1_cake_to_html(cake_1, './cake_1.html')

# Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
# Cake.export_all_cakes_to_html('./all_cakes.html')



# for c in Cake.bakery_offer:
#     c.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, c)

# for c in Cake.bakery_offer:
#     c.export_this_cake_to_html('./{}.html'.format(c.name.replace('', '_')))

# #***************************************************************************************