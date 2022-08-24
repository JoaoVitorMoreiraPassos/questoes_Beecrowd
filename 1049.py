all = {
    'vertebrado': {'ave':{'carnivoro' : 'aguia', 'onivoro' : 'pomba'},
                   'mamifero':{'onivoro': 'homem', 'herbivoro': 'vaca'}},
    'invertebrado': {'inseto': {'hematofago': 'pulga', 'herbivoro': 'lagarta'},
                     'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca' }}
}
classe = input()
tipo = input()
come = input()
print(all[classe][tipo][come])