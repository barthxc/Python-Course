class Pajaro:
    alas = True
    #contructor init
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        #Es como this.nombre = nombre
#Métodos
    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")



piolin=Pajaro('amarillo','canario')
piolin.piar()
piolin.volar(34)