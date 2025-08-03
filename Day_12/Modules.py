import random
import string

# 1. Génération d'un ID utilisateur aléatoire
def random_user_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# 2. Génération d'IDs personnalisés
def user_id_gen_by_user():
    char_count = int(input("Nombre de caractères par ID: "))
    id_count = int(input("Nombre d'ID à générer: "))
    
    ids = []
    for _ in range(id_count):
        ids.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=char_count)))
    
    return ids

# 3. Génération de couleur RGB
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b})'



#exercice : niveau 2
# 1. Liste de couleurs hexadécimales
def list_of_hexa_colors(n=1):
    return ['#' + ''.join(random.choices('0123456789ABCDEF', k=6)) for _ in range(n)]

# 2. Liste de couleurs RGB
def list_of_rgb_colors(n=1):
    return [rgb_color_gen() for _ in range(n)]

# 3. Générateur de couleurs
def generate_colors(color_type, count):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(count)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(count)
    else:
        raise ValueError("Type de couleur non supporté. Utilisez 'hexa' ou 'rgb'")
    
    
    
    

#Exercice : niveau 3
# 1. Mélanger une liste
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

# 2. Tableau de nombres uniques
def unique_random_numbers():
    return random.sample(range(10), 7)

# Niveau 1
print("1. ID aléatoire:", random_user_id())  # Ex: '1EEE33D'

print("\n2. Génération personnalisée:")
# Testez avec les inputs: 5 et 3
print(user_id_gen_by_user())

print("\n3. Couleur RGB:", rgb_color_gen())  # Ex: rgb(125, 244, 255)

# Niveau 2
print("\nHexa colors:", list_of_hexa_colors(3))  # Ex: ['#a3e12f', '#03ed55', '#eb3d2b']
print("RGB colors:", list_of_rgb_colors(2))     # Ex: ['rgb(5,55,175)', 'rgb(50,105,100)']
print("Generate colors:", generate_colors('hexa', 1)) # Ex: ['#b334ef']

# Niveau 3
print("\nListe mélangée:", shuffle_list([1, 2, 3, 4, 5]))  # Ex: [3, 1, 5, 2, 4]
print("Nombres uniques:", unique_random_numbers())          # Ex: [7, 3, 9, 0, 2, 5, 1]