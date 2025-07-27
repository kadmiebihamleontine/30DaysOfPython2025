#Exercices: niveau 2
# 1. Liste vide
liste_vide = []

# 2. Liste avec 5 éléments
liste_5 = [1, 2, 3, 4, 5]

# 3. Longueur de liste
print(len(liste_5))  # 5

# 4. Premier, moyen et dernier élément
print(liste_5[0], liste_5[len(liste_5)//2], liste_5[-1])

# 5. Liste mixte
mixed_data_types = ["Jean", 30, 1.75, "célibataire", "Paris"]

# 6-7. Liste d'entreprises
IT_COMPANIES = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(IT_COMPANIES)

# 8. Nombre d'entreprises
print(len(IT_COMPANIES))  # 7

# 9. Première, moyenne et dernière entreprise
print(IT_COMPANIES[0], IT_COMPANIES[len(IT_COMPANIES)//2], IT_COMPANIES[-1])

# 10. Modification et affichage
IT_COMPANIES[0] = "Meta"
print(IT_COMPANIES)

# 11. Ajout en fin
IT_COMPANIES.append("Tesla")

# 12. Insertion au milieu
IT_COMPANIES.insert(len(IT_COMPANIES)//2, "Samsung")

# 13. Modification (sauf IBM)
for i in range(len(IT_COMPANIES)):
    if IT_COMPANIES[i] != "IBM":
        IT_COMPANIES[i] = IT_COMPANIES[i].upper()

# 15. Vérification existence
print("Google" in IT_COMPANIES)  # True

# 16. Tri
IT_COMPANIES.sort()

# 17. Inversion
IT_COMPANIES.reverse()

# 18-19. Suppression éléments
del IT_COMPANIES[:3]  # 3 premiers
del IT_COMPANIES[-3:]  # 3 derniers

# 20. Tranche du milieu
milieu = IT_COMPANIES[len(IT_COMPANIES)//2-1:len(IT_COMPANIES)//2+2]

# 26-27. Concaténation et insertion
full_stack = 'front_end' + 'back_end'
full_stack.insert(full_stack.index("redux")+1, "Python")
full_stack.insert(full_stack.index("Python")+1, "SQL")




#Exercices: niveau 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Tri et min/max
ages.sort()
min_age, max_age = min(ages), max(ages)
ages.extend([min_age, max_age])

# Médiane
median = (ages[len(ages)//2] + ages[~(len(ages)//2)]) / 2

# Moyenne
moyenne = sum(ages)/len(ages)

# Pays
pays = ['Chine', 'Russie', 'USA', 'Finlande', 'Suède', 'Norvège', 'Danemark']
pays_scandinaves = pays[3:]  # Finlande, Suède, Norvège, Danemark


#Exercices: niveau 3
# 1. Pays du milieu
pays_du_milieu = pays[len(pays)//2] if len(pays)%2 else pays[len(pays)//2-1:len(pays)//2+1]

# 2. Division en deux
if len(pays)%2 == 0:
    moitie1, moitie2 = pays[:len(pays)//2], pays[len(pays)//2:]
else:
    moitie1, moitie2 = pays[:len(pays)//2+1], pays[len(pays)//2+1:]