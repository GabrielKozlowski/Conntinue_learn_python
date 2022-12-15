


class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)

    def __str__(self):
        return "Kind: {}, Name: {}, Additives: {}".format(self.kind, self.name, self.additives)

    def __iadd__(self, texts):
        additives = self.additives
        if type(texts) == int or type(texts) == dict or type(texts) == bool:
            return "This type: {} canot be added to an object".format(type(texts))
        else:    
            if type(texts) == tuple or type(texts) == list:               
                additives.extend(texts)
            else:
                additives.append(texts)
        
            return (self.name, self.kind, self.taste, self.additives, self.filling)

cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake01 += 'sprinkles', 'cherries'
print(cake01)







