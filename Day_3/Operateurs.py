#1/
Age = 19
#2/
Taille = 1.52
#3/
Num_complex = 8-1J
'''4/
base = float(input("Entrez la base: "))
hauteur = float(input("Entrez la hauteur: "))
aire = 0.5 * base * hauteur
print(f"La zone du triangle est de {aire}")'''
'''5/
a = float(input("Entrez le coté A: "))
b = float(input("Entrez le coté B: "))
c = float(input("Entrez le coté C: "))
perimetre = a + b + c
print(f"Le périmètre du triangle est {perimetre}")'''

#6/
longueur = float(input("Entrez la longueur d'un rectangle: "))
largeur = float(input("Entrez la largeur d'un rectangle: "))
surface = longueur * largeur
périmètre = 2 * (longueur + largeur)
print(f"Le périmètre du rectangle est {périmètre}")
print(f"La surface du rectangle est {surface}")

#7/
rayon = float(input("Entrez le rayon du cercle : "))
pi = 3.14
zone = pi * rayon ** 2
circonference = 2 * pi * rayon
print(f"Zone: {zone}, Circonférence: {circonference}")

#8/
# y = 2x - 2
pente = 2
ordonnee_y = -2  # quand x=0
ordonnee_x = 1    # solution de 0 = 2x - 2 => x=1
#9/
x1, y1 = 2, 2
x2, y2 = 6, 10
pente = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Pente: {pente}, Distance: {distance}")
#10/
print("Les pentes sont égales" if pente == 2 else "Les pentes sont différentes")
#11/
# Solution pour y=0: x² + 6x + 9 = 0 => (x+3)² = 0 => x=-3
x = float(input("Entrez la valeur de x : "))
y = x**2 + 6*x + 9
print(f"Pour x={x}, y={y}")
#12/
print(len("Python") == len("Dragon"))  # False (6 != 6) → En fait True, correction:
print(len("Python") > len("Dragon"))   # False (6 > 6 → False)
#13/
print('on' in 'python' and 'on' in 'dragon')  # True
#14/
phrase = "I hope this course is not full of jargon."
print('jargon' in phrase)  # True
#15/
print(not ('on' in 'dragon' and 'on' in 'python'))  # False (car les deux contiennent 'on')
#16/
longueur = len("python")
float_version = float(longueur)
print(float_version)  # 6.0
#17/
nombre = int(input("Entrez un nombre : "))
if nombre % 2 == 0:
    print(f"{nombre} est pair.")
else:
    print(f"{nombre} est impair.")
#18/
print(7 // 3 == int(2.7))  # True (car 7 // 3 = 2 et int(2.7) = 2)
#19/
print(type("10") == type(10))  # False (str ≠ int)
#20/
# Erreur : int('9.8') échoue car Python ne convertit pas directement les strings float en int.
# Correction :
print(int(float('9.8')) == 10)  # False (car int(9.8) = 9)
#21/
heures = float(input("Entrez les heures travaillées : "))
taux = float(input("Entrez le taux horaire : "))
salaire = heures * taux
print(f"Votre gain hebdomadaire est de {salaire}")
#22/
annees = int(input("Entrez le nombre d'années vécues : "))
secondes = annees * 365 * 24 * 60 * 60  # 1 an = 365 jours × 24h × 60min × 60s
print(f"Vous avez vécu {secondes} secondes.")
#23/
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)