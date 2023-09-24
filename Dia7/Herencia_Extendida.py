class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color=color
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")



class Pajaro(Animal):
    #HAY 2 FORMAS DE CREAR ATRIBUTOS EN UNA CLASE HEREDERA
        #1 Usando metodo init
    def __init__(self, edad, color , altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
         #2 EN VEZ DE DESCRIBIR NUEVAMENTE LOS ATRIBUTOS DEL PASE USAMOS SUPER
    def __init__(self, edad, color, altura_vuelo):
        super.__init__(edad,color)
        self.altura_vuelo = altura_vuelo
    #Pajaro puede tener 3 tipos de métodos:
        #Los heredados de su padre ANIMAL
        #METODOS HEREDADOS PERO MODIFICADO COMO HABLAR

    def hablar(self):
        print('pio')
    def volar(self,metros):
        print(f"El pajaro vuela {metros} metros")
piolin = Pajaro(3,'amarillo', 60)

piolin.hablar()
piolin.volar(100)

mi_animal = Animal(20, 'negro')

