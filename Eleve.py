class Eleve:
    def __init__(self, nom, prenom, age, formation, note):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.formation = formation
        self.note = note

    def admission(self):
        if self.note >= 10:
            print("Admis")
        else:
            print("Non admis")

    def verifAge(self):
        if self.age >= 18:
            print("Eligible à la formation")
        else:
            print("Non-éligible à la formation")