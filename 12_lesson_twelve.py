import pickle
import glob

class Cake:

    known_kinds = ['cake', 'waffle', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []


    def __init__(self, name, kind, taste, additves, filling, gluten_free, text) -> None:
        self.name = name
        if kind in self.known_kinds:
            self.kind = "other" 
        else:
            self.kind = kind
        self.taste = taste
        self.additves = additves.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
        if kind == 'cake with apples' or text == '':
            self.__text = text
        else:
            self.__text = ''
            
        Cake.bakery_offer.append(self)

    def show_info(self):
        print('{}'.format(self.name).upper())
        print('Kind: {}'.format(self.kind))
        print('Taste: {}'.format(self.taste))
        if len(self.additves) > 0:
            print('Additves:')
            for additive in self.additves:
                print('\t{}'.format(additive))
        if len(self.filling) > 0:
            print('Filling: \n\t{}'.format(self.filling))
        else:
            print('Filling: ')
        print('Glutten free: {}'.format(self.__gluten_free)) 
        if len(self.__text) > 0:
            print('Text on: "{}" is: \n[{}]'.format(self.kind, self.__text))


    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additves):
        self.additves.extend(additves) 

    def __get_text(self):
        return self.__text
    
    def __set_text(self, new_text):
        if self.kind == 'cake with apples':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake with apples ({})<<<<<'.format(self.name))
    
    Text = property(__get_text, __set_text, None, 'Text changed')


    def save_to_file(self,path):
        with open(path, 'wb') as f:
            pickle.dump(self,f)

    @classmethod
    def read_from_file(cls,path):
        with open(path, 'rb') as f:
            newObject = pickle.load(f)
            cls.bakery_offer.append(newObject)
            return newObject

    @staticmethod
    def get_bakery_file(catalogName):
        return glob.glob(catalogName + '*.bakery')
        
   
        
        


cake_1 = Cake('Apple_pie', 'cake with apples', 'apple', ['castor sugar'], '', False, 'Love you')
cake_2 = Cake('Pickaninny_pie', 'black cake', 'cacao', ['icing', 'nuts'], 'chocolade', False, '')
cake_3 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake_4 = Cake('Cocoa waffle','waffle','cocoa', [],'cocoa', False, '')


cake_1.save_to_file('./cake1.bakery')
cake_2.save_to_file('./cake2.bakery')


print('-'* 50)

print('Today in our offer:\n')
for c in Cake.bakery_offer:
    Cake.show_info(c)
    print()


print('-+'* 50)
cake_5 = Cake.read_from_file('./cake1.bakery')
Cake.show_info(cake_5)

print()
print(Cake.get_bakery_file('./'))