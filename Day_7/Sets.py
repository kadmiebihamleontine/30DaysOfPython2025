#Exercices Niveau 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#1/
len(it_companies)  # Réponse : 7
#2/
it_companies.add("Twitter")
#3/
it_companies.update(["Samsung", "Tesla", "Netflix"])
#4/
it_companies.remove("IBM")  # Lève une erreur si l'élément n'existe pas
'''5/
remove() : Supprime un élément et lève une erreur (KeyError) s'il n'existe pas.

discard() : Supprime un élément sans erreur si l'élément est absent.'''

#Exercices Niveau 2 
#1/
A.union(B)  # ou `A | B`
# Réponse : {19, 20, 22, 24, 25, 26, 27, 28}
#2/
A.intersection(B)  # ou `A & B`
# Réponse : {19, 20, 22, 24, 25, 26}
#3/
A.issubset(B)  # Réponse : True (car tous les éléments de A sont dans B)
#4/
A.isdisjoint(B)  # Réponse : False (car ils ont des éléments communs)
#5/
#Les deux opérations donnent le même résultat (l'union est commutative).
#6/
A.symmetric_difference(B)  # ou `A ^ B`
# Réponse : {27, 28} (éléments présents dans un seul des deux ensembles)
#7/
del A
del B


#Exercices Niveau 3
#1/
age_set = set(age)
len(age)      # Réponse : 8 (car la liste peut avoir des doublons)
len(age_set)  # Réponse : 5 (car les doublons sont supprimés)
# L'ensemble est plus petit car il ne garde que les valeurs uniques.
#2/
#3/
phrase = "I am a teacher and I love to inspire and teach people"
mots = phrase.split()  # Séparation en mots
mots_uniques = set(mots)  # Conversion en ensemble pour éliminer les doublons
len(mots_uniques)  # Réponse : 10
# Mots uniques : {'I', 'am', 'a', 'teacher', 'and', 'love', 'to', 'inspire', 'teach', 'people'}