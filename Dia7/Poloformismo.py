class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + ' dime muuu')



class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + ' dime bee')

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

animales = [vaca1,oveja1]

for animal in animales:
    animal.hablar()

def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)


class Mago():
    def defender(self):
        print("Escudo mágico")


class Arquero():
    def defender(self):
        print("Esconderse")


class Samurai():
    def defender(self):
        print("Bloqueo")


def personaje_defender(personaje):
    personaje.defender()


mago1 = Mago()
arquero1 = Arquero()
samurai1 = Samurai()

personaje_defender(mago1)
personaje_defender(arquero1)
personaje_defender(samurai1)