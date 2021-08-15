import turtle
from skills import Skills
import matplotlib.pyplot as plt
import math

# Calculer la vitesse
"""temps = 6.892
distance = 19.7

vitesse = distance / temps
print(math.ceil(vitesse))
"""
# Afficher profil / Insertion utilisateur
"""nom = input("Votre nom: ")
age = input("Votre age: ")

print("Votre nom est : " + nom + " ,et vous avez " + age + "ans.")
"""
# Listes
"""paires = ["Jordan mid air", "Converse", "Nike"]

print(paires[-2])
print(paires[0:2])
"""

# Fonctions
"""
def add_number(a, b):
  return a + b

print(add_number(5, 2))
"""

# If statements
"""
age = input("Enter your age: ")
id_card = input("Valid: ")

if int(age) >= 18 and id_card == 'Yes':
    print("You can enter")
elif int(age) >= 18 and not id_card == 'No':
    print("You're id card is not valid")
else:
    print("Access denied")
"""

# While
'''edo_beau = input("Est ce que Edo est beau : ")

while edo_beau == "Ouais, il est beau":
    print("C'est bien")
    break
'''
# For
'''
paires = ["Jordan mid air", "Converse", "Nike"]
for paire in paires:
    print(paire) # Affiche à chque itérations chaque élément de la liste
'''
# Try except
"""
try:
    number = int(input("Entrez un nombre: "))
    print(number)
except:
    print("Invalid Input")
"""

# Importation classes et création d'objets
'''
from Eleve import Eleve

eleve1 = Eleve("Temesgen", "Edomiyas", 20, "Informatique", 15)

print(eleve1.nom, eleve1.prenom, eleve1.age, eleve1.formation, eleve1.note)
#Eleve.admission(eleve1)
eleve1.admission()
'''

# Tableaux entraînement
'''
t = [2,3,4,5,6,7,8]
t.sort(reverse=True)
print(t)
'''
'''
t = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
i = input("Saisir une valeur : ")

while 0 > int(i) > 20:
    print("Resaisissez une valeur positif !")
    break
'''
'''
n = int(input().strip())

for i in range(1, 11):
    result = n * i
    print(str(n) + " x " + str(i) + " = " + str(result))
'''

'''
a = input("Saissisez un nombre: ")
b = input("Saissisez un autre nombre: ")

c = int(a) + int(b)

print("Voici la somme des deux numéros: " + str(c))
'''

'''from Eleve import Eleve
Edomiyas = Eleve("Temesgen", "Edomiyas", 21, "Responsable de l'inginerie des logiciels", 15)

print(Edomiyas.nom, Edomiyas.prenom, Edomiyas.age, Edomiyas.formation, Edomiyas.note)
Edomiyas.admission()
Edomiyas.verifAge()
'''

'''
print("I don't know if i'm progressing ?")

guess = input("Guessing...")

if guess == "yes":
    print("Yes, you are !")
else:
    print("Don't dought your self ever !")
'''

'''Graphs
size_of_groups = [70, 50, 30, 45, 50, 20]


plt.pie(size_of_groups)
plt.show()
'''

'''project
mySkills = Skills(70, 50, 30, 45, 50, 20)

mySkills.progression()
'''

# input graphics

screen = turtle.Screen()
screen.setup(400, 300)
language = turtle.textinput("Home page", "Tech")
progression = turtle.textinput("", "Progression")


print(language)
print(progression)
