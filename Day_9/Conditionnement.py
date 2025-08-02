#Exercice : level1
#1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")
#2
my_age = 25  # Vous pouvez modifier cet âge selon votre cas
your_age = int(input("Enter your age: "))

if your_age > my_age:
    diff = your_age - my_age
    if diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {diff} years older than me.")
elif your_age < my_age:
    diff = my_age - your_age
    if diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {diff} years older than you.")
else:
    print("We are the same age!")
#3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")


#Exercice : niveau2
#1/
score = int(input("Enter your score (0-100): "))

if score >= 80 and score <= 100:
    grade = 'A'
elif score >= 70 and score <= 89:
    grade = 'B'
elif score >= 60 and score <= 69:
    grade = 'C'
elif score >= 50 and score <= 59:
    grade = 'D'
elif score >= 0 and score <= 49:
    grade = 'F'
else:
    grade = 'Invalid score'

print(f"Your grade is: {grade}")
#2/
month = input("Enter a month: ").lower()

if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Unknown month'

print(f"The season is: {season}")
#3/
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()

if new_fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(new_fruit)
    print("Modified list:", fruits)
    

#Exercice : level3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1. Check for skills key and print middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# 2. Check if person has Python skill
if 'skills' in person and 'Python' in person['skills']:
    print("The person has Python skill")

# 3. Determine developer type
if 'skills' in person:
    skills_set = set(person['skills'])
    
    if skills_set == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif skills_set >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif skills_set >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('unknown title')

# 4. Print marriage and country info
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")