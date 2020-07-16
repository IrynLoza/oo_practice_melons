############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        
        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)
      

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('mint')
    casaba.add_pairing('strawberries')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Crenshaw')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    melon_types = make_melon_types()

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        #itterate nasted list [[], [], [], []] 
        for pair in melon.pairings:
            print(f'-{pair}')

print_pairing_info(make_melon_types())       
    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    code_dict = {}
    
    for melon in melon_types:
        code_dict[melon.code] = melon

    #print(code_dict)
    return code_dict

#make_melon_type_lookup(make_melon_types())


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melons_by_id, shape_rating, color_rating, harvest_from_field, harvest_by):
                """Initialize a melon."""

                self.melons_by_id = make_melon_type_lookup(make_melon_types())

                self.shape_rating = shape_rating
                self.color_rating = color_rating
                self.harvest_from_field = harvest_from_field
                self.harvest_by = harvest_by

    def is_sellable(self): 
        """Check if melons are sellable""" 

        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_from_field != 3:
            return True    
        return False    


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    all_melons = []

    melon_1 = Melon([3], 8, 7, 2, 'Sheila')
    all_melons.append(melon_1)

    melon_2 = Melon([3], 3, 4, 2, 'Sheila')
    all_melons.append(melon_2) 

    melon_3 = Melon([3], 9, 8, 3, 'Sheila')
    all_melons.append(melon_3)

    melon_4 = Melon([1], 10, 6, 35, 'Sheila')
    all_melons.append(melon_4)

    melon_5 = Melon([2], 8, 9, 35, 'Michael')
    all_melons.append(melon_5)

    melon_6 = Melon([2], 8, 2, 35, 'Michael')
    all_melons.append(melon_6)

    melon_7 = Melon([2], 2, 3, 4, 'Michael')
    all_melons.append(melon_7)

    melon_8 = Melon([0], 6, 7, 4, 'Michael')
    all_melons.append(melon_8)

    melon_9 = Melon([3], 7, 10, 3, 'Sheila')
    all_melons.append(melon_9)
    
    return all_melons
   

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    sellability = '' 
    for melon in melons: 
        if melon.is_sellable() == True:
            sellability = '(CAN BE SOLD)'
            print(f'Harvested by {melon.harvest_by} from Field {melon.harvest_from_field} {sellability}')
        else:
            sellability = '(NOT SELLABLE)'
            print(f'Harvested by {melon.harvest_by} from Field {melon.harvest_from_field} {sellability}')       

get_sellability_report(make_melons(make_melon_types()))


