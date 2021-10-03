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
#print (*vulZak1)            # hashtag omdat ik wil testen met de andere functions. remove # als je deze wil testen



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
#print (vulZak2)            # hashtag omdat ik wil testen met de andere functions. remove # als je deze wil testen

def sorteren (x):
    #x.sort()                            # dit werkt alleen met een list! dus vulZak1. niet met dictionary vulZak2
    sorteerzak = sorted(x)   # wat is de opdracht precies? moet ik elke individuele m&m printen, of alleen de 4 kleuren in volgorde van hoeveelheid
    print (sorteerzak)

sorteren(vulZak1)          # hashtag omdat ik wil testen met de andere functions. remove # als je deze wil testen