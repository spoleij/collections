from typing import List
import random
kleuren = ['oranje' , 'blauw' , 'groen' , 'bruin']

aantal = int(input ('Hoeveel kleuren M&M’s moeten er aan de zak worden toegevoegd?\n'))

def maakDict(x :int):
    vulZak2 = {}
    for i in range (x):
        grabbelen = (random.choice(kleuren))
        #vulZak2[grabbelen] = 1                 ##########OKE DE FOUT LAG DE HELE TIJD BIJ DEZE REGEL!!! DIT MOEST GEWOON WEG. 
        if grabbelen in vulZak2.keys():
            vulZak2 [grabbelen] = vulZak2 [grabbelen] + 1 
        else:
            vulZak2 [grabbelen] = 1 
    print('Je zak M&Ms bestaat uit de volgende kleuren:')               
    return vulZak2
                                # {} maakt lege dictionary
vulZak2 = maakDict(aantal)
print (vulZak2)            