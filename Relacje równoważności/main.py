class Atom:
    def __init__(self, value, relations):
        self.relations_to = []
        self.relations_from = []
        self.value = value
        for i in relations:
            if i[0] == value:
                self.relations_from.append(i)
            if i[1] == value:
                self.relations_to.append(i)

    def is_callback(self):
        if [self.value, self.value] in self.relations_to:
            return True
        else:
            return False

    def is_symetrical(self):
        missing = []
        for i in self.relations_to:
            if not i[::-1] in self.relations_from:
                missing.append(i[::-1])
        return missing

f = open("input.txt", "r")
Atoms_input = f.readline()[:-1].split(', ')
Relations_input = f.readline().split(';')

if Relations_input == ['']:
    Relations_input = []

Relations = [i.split(',') for i in Relations_input]

Atoms = []
for i in Atoms_input:
    Atoms.append(Atom(i, Relations))

#sprawdzenie zwrotności
callback_missing = []
for atom in Atoms:
    if not atom.is_callback():
        callback_missing.append([atom.value, atom.value])

#sprawdzenie symetrycznosci
symetry_missing = []
for atom in Atoms:
    pom = atom.is_symetrical()
    if pom:
        symetry_missing.append(pom)

#sprawdzenie tranzytywności
transity_missing = []
for atom in Atoms:
    for relation_from in atom.relations_from:
        for relation_to in atom.relations_to:
            if not [relation_to[0], relation_from[1]] in Relations and relation_to[0] != relation_from[1]:
                transity_missing.append([relation_to[0], relation_from[1]])

if not (callback_missing or symetry_missing or transity_missing):
    print("Podana relacja jest relacją równoważności")
else:
    if callback_missing:
        print("Domknięcie zwrotne:")
        print(callback_missing)
    if symetry_missing:
        print("Domknięcie symetryczne:")
        print(symetry_missing)
    if transity_missing:
        print("Domknięcie tranzytywne:")
        print(transity_missing)