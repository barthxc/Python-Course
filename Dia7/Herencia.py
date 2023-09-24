class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color=color
    def nacer(self):
        print("Este animal ha nacido")
    pass



class Pajaro(Animal):
    pass

print(Pajaro.__base__) #Para saber la herencia de laclase. Pajaro hereda de animal
print(Animal.__subclasses__()) #Para ver las clases que tiene animal como padre que es

piolin = Pajaro(20,'rojo')
piolin.nacer()

print(piolin.color)