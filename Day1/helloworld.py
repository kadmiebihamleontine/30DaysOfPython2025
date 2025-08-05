from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Différence entre map, filter, reduce
"""
- map: Applique une fonction à chaque élément d'un itérable
- filter: Filtre les éléments selon une condition
- reduce: Combine les éléments en appliquant une fonction cumulative
"""

# 2. Différence entre HOF, closure et décorateur
"""
- Higher Order Function: Fonction qui prend/retourne une fonction
- Closure: Fonction interne qui garde accès aux variables locales même après exécution
- Decorator: Fonction qui modifie une autre fonction (utilise @notation)
"""

# 3. Fonction call avant map/filter/reduce
def square(x):
    return x ** 2

squared_numbers = list(map(square, numbers))

# 4-6. Boucles for
for country in countries:
    print(country)

for name in names:
    print(name)

for num in numbers:
    print(num)
    

#€xercice 2
# 1. Pays en majuscules
uppercase_countries = list(map(str.upper, countries))

# 2. Nombres au carré
squared_numbers = list(map(lambda x: x**2, numbers))

# 3. Noms en majuscules
uppercase_names = list(map(str.upper, names))

# 4. Filtre 'land'
land_countries = list(filter(lambda c: 'land' in c.lower(), countries))

# 5. Exactement 6 caractères
six_char_countries = list(filter(lambda c: len(c) == 6, countries))

# 6. Six lettres ou plus
six_plus_countries = list(filter(lambda c: len(c) >= 6, countries))

# 7. Commençant par 'E'
e_countries = list(filter(lambda c: c.startswith('E'), countries))

# 8. Chaînage d'itérateurs
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# 9. Filtre de chaînes
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

# 10. Somme avec reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)

# 11. Concaténation pays
sentence = reduce(lambda x, y: f"{x}, {y}", countries[:-1]) + f" and {countries[-1]} are north European countries"

# 12. Catégorisation pays
def categorize_countries(pattern):
    return [c for c in countries if pattern.lower() in c.lower()]

# 13. Dictionnaire par initiale
def country_initial_counts():
    initials = [c[0].upper() for c in countries]
    return {letter: initials.count(letter) for letter in set(initials)}

# 14-15. Premiers/derniers pays
def get_first_ten_countries():
    return countries[:10]

def get_last_ten_countries():
    return countries[-10:]

#€xercice 3
from data.countries_data import countries_data

# Tri par nom, capitale, population
countries_by_name = sorted(countries_data, key=lambda x: x['name'])
countries_by_capital = sorted(countries_data, key=lambda x: x['capital'])
countries_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

# 10 langues les plus parlées
language_counts = {}
for country in countries_data:
    for lang in country['languages']:
        language_counts[lang] = language_counts.get(lang, 0) + 1

top_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# 10 pays les plus peuplés
top_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]