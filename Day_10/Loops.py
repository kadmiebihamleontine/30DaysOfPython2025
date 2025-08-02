#Exercices Niveau 1
#1/
# Avec for
for i in range(11):
    print(i)

# Avec while
i = 0
while i <= 10:
    print(i)
    i += 1
#2/
# Avec for
for i in range(10, -1, -1):
    print(i)

# Avec while
i = 10
while i >= 0:
    print(i)
    i -= 1
#3/
for i in range(1, 8):
    print("#" * i)
#4/
for _ in range(5):
    print("# " * 13)
#5/
for i in range(11):
    print(f"{i} x {i} = {i * i}")
#6/
frameworks = ["python", "numpy", "pandas", "django", "flask"]
for framework in frameworks:
    print(framework)
#7/
for i in range(0, 101, 2):
    print(i)
#8/
for i in range(1, 101, 2):
    print(i)


#Exercices Niveau 2
#1/
total = 0
for i in range(101):
    total += i
print(f"La somme de tous les nombres est {total}.")  # 5050
#2/
sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"Somme des pairs: {sum_even}")  # 2550
print(f"Somme des impairs: {sum_odd}")  # 2500


#exercice niveau 3
#1/
