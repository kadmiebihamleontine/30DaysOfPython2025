#Exercices: niveau 1
#1/
def add_two_numbers (a, b):
    return a+b
#2/
def area_of_circle (r, π = 3.14):
    return π * r * r
# 3. Somme de nombres variables
def add_all_nums(*args) -> float:
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
            return "Tous les arguments doivent être des nombres"
        total += num
    return total

# 4. Conversion Celsius en Fahrenheit
def convert_celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

# 5. Saison selon le mois
def check_season(month: str) -> str:
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Autumn'

# 6. Calcul de la pente
def calculate_slope(x1: float, y1: float, x2: float, y2: float) -> float:
    return (y2 - y1) / (x2 - x1)

# 7. Équation quadratique
def solve_quadratic_eqn(a: float, b: float, c: float) -> tuple:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Pas de solution réelle"
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)

# 8. Affichage d'une liste
def print_list(lst: list) -> None:
    for item in lst:
        print(item)

# 9. Inversion de liste (avec boucle)
def reverse_list(arr: list) -> list:
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

# 10. Capitalisation des éléments de liste
def capitalize_list_items(lst: List[str]) -> List[str]:
    return [item.capitalize() for item in lst]

# 11. Ajout d'élément à une liste
def add_item(lst: list, item) -> list:
    lst.append(item)
    return lst

# 12. Suppression d'élément d'une liste
def remove_item(lst: list, item) -> list:
    if item in lst:
        lst.remove(item)
    return lst

# 13. Somme des nombres jusqu'à n
def sum_of_numbers(n: int) -> int:
    return sum(range(1, n+1))

# 14. Somme des nombres impairs jusqu'à n
def sum_of_odds(n: int) -> int:
    return sum(i for i in range(1, n+1) if i % 2 != 0)

# 15. Somme des nombres pairs jusqu'à n
def sum_of_even(n: int) -> int:
    return sum(i for i in range(1, n+1) if i % 2 == 0)

#Exercices: niveau 2
# # 1. Compter les nombres pairs et impairs
def evens_and_odds(n: int) -> str:
    evens = n // 2 + 1 if n % 2 == 0 else (n + 1) // 2
    odds = n // 2
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

# 2. Calcul factoriel
def factorial(num: int) -> int:
    if num < 0:
        return "Input must be non-negative"
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# 3. Vérifier si vide
def is_empty(data: Any) -> bool:
    if data is None:
        return True
    if isinstance(data, (list, dict, set, tuple, str)):
        return len(data) == 0
    return False

# 4. Fonctions statistiques
def calculate_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

def calculate_median(numbers: List[float]) -> float:
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def calculate_mode(numbers: List[float]) -> List[float]:
    count = Counter(numbers)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count]

def calculate_range(numbers: List[float]) -> float:
    return max(numbers) - min(numbers)

def calculate_variance(numbers: List[float]) -> float:
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std(numbers: List[float]) -> float:
    return (calculate_variance(numbers))**(1/2)

#Exercices: niveau 3
# 1. Vérifier si un nombre est premier
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int((n)**(1/2)) + 1, 2):
        if n % i == 0:
            return False
    return True

# 2. Vérifier si tous les éléments sont uniques
def all_unique(lst: list) -> bool:
    return len(lst) == len(set(lst))

# 3. Vérifier si tous les éléments sont du même type
def same_data_type(lst: list) -> bool:
    return all(isinstance(item, type(lst[0])) for item in lst) if lst else True

# 4. Vérifier si une chaîne est un identifiant Python valide
def is_valid_variable(name: str) -> bool:
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True

# 5. Fonctions pour les données pays (à utiliser avec countries-data.py)
def most_spoken_languages(countries, n=10):
    lang_count = {}
    for country in countries:
        for language in country["languages"]:
            lang_count[language] = lang_count.get(language, 0) + country["population"]
    
    sorted_languages = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

def most_populated_countries(countries, n=10):
    sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)
    return [(c["name"], c["population"]) for c in sorted_countries[:n]]