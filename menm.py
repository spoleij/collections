from typing import List
import random

kleuren = ['oranje' , 'blauw' , 'groen' , 'bruin']

aantal = int(input ('Hoeveel kleuren M&M’s moeten er aan de zak worden toegevoegd?\n'))

def maakList(aantal :int):
    vulZak = []
    for i in range (aantal):
        vulZak.append (random.choice(kleuren))                 # de asteriks * print de list inhoud, zonder [] en ' '
    return vulZak

vulZak = maakList(aantal)
print('Je zak M&Ms bestaat uit de volgende kleuren:')
print (*vulZak)

