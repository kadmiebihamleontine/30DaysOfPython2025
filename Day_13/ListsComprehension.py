#1
nombres = [-4, -3, -2, -1, 0, 2, 4, 6]
filtres = [n for n in nombres if n <= 0]
print(filtres)  # Output: [-4, -3, -2, -1, 0]
#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
aplati = [num for sous_liste in list_of_lists 
          for sous_sous_liste in sous_liste 
          for num in sous_sous_liste]
print(aplati)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#3
liste_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(liste_tuples)
# Output: [(0, 1, 0, 0, 0, 0, 0), (1, 1, 1, 1, 1, 1, 1), ..., (10, 1, 10, 100, 1000, 10000, 100000)]
#4
pays = [[('Finlande', 'Helsinki')], [('Suède', 'Stockholm')], [('Norvège', 'Oslo')]]
transforme = [[pays[0], pays[0][:3], ville[0]] for [[pays, ville]] in pays]
print(transforme)
# Output: [['Finlande', 'Fin', 'Helsinki'], ['Suède', 'Swe', 'Stockholm'], ['Norvège', 'Nor', 'Oslo']]
#5
pays = [[('Finlande', 'Helsinki')], [('Suède', 'Stockholm')], [('Norvège', 'Oslo')]]
dict_pays = [{'country': p, 'city': v} for [[p, v]] in pays]
print(dict_pays)
# Output: [{'country': 'Finlande', 'city': 'Helsinki'}, ...]
#6
noms = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenes = [f"{prenom} {nom}" for [[prenom, nom]] in noms]
print(concatenes)
# Output: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#7
# Fonction lambda pour calculer la pente (m) entre deux points
pente = lambda x1, y1, x2, y2: (y2 - y1)/(x2 - x1)

# Fonction lambda pour calculer l'interception y (b)
interception_y = lambda x, y, m: y - m * x

# Exemple d'utilisation:
m = pente(1, 2, 3, 4)
b = interception_y(1, 2, m)
print(f"Equation: y = {m}x + {b}")  # Output: y = 1.0x + 1.0