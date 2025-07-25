#Jour2: 30 Days of Python Programming

#Exercices: niveau 1
Premier_prenom = 'Léontine'
Nom_de_famille = 'KADMIE'
Nom_complet = 'KADMIE Léontine'
Pays_origine = 'Togo'
Municipalite = 'Lomé'
Age = 19
Es_Marie = False
is_true = True
IS_light_on = False
Multiple = 'Tina', 'est son surnom','Fried',250,True

#Exercices: niveau 2
#1/
print(type(Premier_prenom))
print(type(Nom_de_famille))
print(type(Nom_complet))
print(type(Pays_origine))
print(type(Municipalite))
print(type(Age))
print(type(Es_Marie))
print(type(is_true))
print(type(IS_light_on))
print(type(Multiple))

#2/
print("La longueur de mon prénom est:",len(Premier_prenom))
#3/
print("le plus petit est :",min(len(Premier_prenom),len(Nom_de_famille)))
#4/
num_one = 5
num_two = 4
#5/
addict = num_one + num_two
print("l'addition donne:",addict)
#6/
soustr = num_two - num_one
print("la soustraction donne:",soustr)
#7/
produit = num_one * num_two
print("Le produit donne:",produit)
#8/
division = num_one / num_two
print("La division donne:",division)
#9/
reste = num_one % num_two
print("Le reste donne:",reste)
#10/
floor_division = num_one // num_two
print("La division entière donne:",floor_division)

#11/
r = 30
#i
area_of_circle = 3.14 * r**2
print(area_of_circle)
#ii
circum_of_circle = 2* 3.14 *r
print(circum_of_circle)
#iii
r = input("Entrez le rayon du cercle:")
area_of_circle = 3.14 * r**2
print(area_of_circle)