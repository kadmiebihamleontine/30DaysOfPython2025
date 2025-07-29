#Exercices: Jour 6
#Exercices: niveau 1
#1/
tuple_vide = ()
#2/
freres = ("Jean", "Paul")
soeurs = ("Marie", "Sophie")
#3/
freres_et_soeurs = freres + soeurs
#4/
nombre_freres_soeurs = len(freres_et_soeurs)
print(nombre_freres_soeurs)  # Output: 4
#5/
parents = ("Pierre", "Lucie")
family_members = freres_et_soeurs + parents
print(family_members)  # Output: ('Jean', 'Paul', 'Marie', 'Sophie', 'Pierre', 'Lucie')


#Exercices: niveau 2
#1/
*freres_soeurs, pere, mere = family_members
print(freres_soeurs)  # ['Jean', 'Paul', 'Marie', 'Sophie']
print(pere, mere)     # Pierre Lucie
#2/
fruits = ("Pomme", "Banane", "Orange")
legumes = ("Carotte", "Tomate", "Poivron")
produits_animaux = ("Lait", "Fromage", "Œufs")
food_stuff_tp = fruits + legumes + produits_animaux
#3/
food_stuff_lt = list(food_stuff_tp)
#4/
milieu = len(food_stuff_lt) // 2
print(food_stuff_lt[milieu])  # "Tomate" (si 9 éléments)
#5/
trois_premiers = food_stuff_lt[:3]
trois_derniers = food_stuff_lt[-3:]
print(trois_premiers, trois_derniers)
#6/
del food_stuff_tp  # Le tuple est supprimé
#7/
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonie est nordique ?", 'Estonia' in nordic_countries)  # False
print("Islande est nordique ?", 'Iceland' in nordic_countries)  # True