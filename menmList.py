from typing import List
import random
kleuren = ['oranje' , 'blauw' , 'groen' , 'bruin']

aantal = int(input ('Hoeveel kleuren M&M’s moeten er aan de zak worden toegevoegd?\n'))

def maakList(x :int):
    vulZak1 = []                                                 # [] naast een variable maakt een lege list!
    for i in range (x):
        vulZak1.append (random.choice(kleuren)) 
    print('Je zak M&Ms bestaat uit de volgende kleuren:')                # de asteriks * print de list inhoud, zonder [] en ' '
    return vulZak1

vulZak1 = maakList(aantal)
print (vulZak1)            
