
# 1
chaine1 = " ".join(["trente", "jours", "de", "python"])
# 2
chaine2 = " ".join(["codage", "pour", "tous"])
# 3
societe = "codage pour tous"
# 4
print(societe)
# 5
print(len(societe))
# 6
print(societe.upper())
# 7
print(societe.lower())
chaine = "Coding For All"
print(chaine.capitalize())
print(chaine.title())
print(chaine.swapcase())
# 9
print(chaine.split()[0])
# 10
print("codage" in societe)
# 11
print(societe.replace("codage", "Python"))
# 12
print("Python pour tout le monde".replace("tout le monde", "tous"))
# 13
print(societe.split())
# 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
# 15
print(chaine[0])
# 16
print(chaine[-1])
# 17
print("codage pour toutes"[10])
# 18
print("".join([mot[0] for mot in "Python pour tout le monde".split()]))
# 19
print("".join([mot[0] for mot in societe.split()]))
# 20
print(societe.index("C"))
# 21
print(societe.index("F"))
# 22
print(societe.rfind("l"))
phrase = "Vous ne pouvez pas mettre fin à une phrase avec parce que parce que c'est une conjonction"
# 23
print(phrase.find("parce que"))
# 24
print(phrase.rindex("parce que"))
# 25-27
print(phrase[phrase.find("parce que"):phrase.rfind("parce que")+len("parce que")])
# 28
print(chaine.startswith("Coding"))
# 29
print(chaine.endswith("coding"))
# 30
print(" Codage pour tous ".strip())
# 31
print("Thirty_days_of_python".isidentifier())  # True
print("30daysofpython".isidentifier())        # False
# 33
print("J'apprécie ce défi.\nJe me demande juste quelle est la prochaine étape.")
# 34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
# 35
print(f"RADIUS = 10\nZone = 3.14 * RADIUS ** 2\nLa zone d'un cercle avec le rayon 10 est de {3.14*10**2} mètres carrés.")
# 36
a, b = 8, 6
print(f"{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} * {b} = {a*b}\n{a} / {b} = {a/b:.2f}\n{a} % {b} = {a%b}\n{a} // {b} = {a//b}\n{a} ** {b} = {a**b}")
