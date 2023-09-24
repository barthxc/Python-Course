#Herramienta para crear tipos de métodos
#Métodos de instancia o normales: Como los que hemos aprendido def saludar(self,nombre)
#Métodos de claseo: Se crea usando @classmethod - def mi_metodo(cls): Pueden ser llamado desde una instancia de la clase o desde la clase.
#NO PUEDEN ACCEDER A LOS ATRIBUTOS DE LA CLASE PERO SI MODIFICARLOS
#Métodos estátidos @staticmethod. No pueden modificar ni instancia ni clase, no usa ni cls ni slef.
#Son como funciones normales agregados a una clase exacta

class Pajaro:
    alas=True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio')

#METOD DE INSTANCIA
    def pintar_negro(self):
        self.color= 'negro'
        print(f"Ahora el pajaro es {self.color}")



    # Métodos de clase. Lo hace la clase, no la instancia
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False  #Puedo acceder a los atributos de clase como ALAS
        print(Pajaro.alas)

        # MÉTODOS ESTÁTICOS
        # No puedo cambiar los atributos de la clase ni de la instancia
    @staticmethod
    def mirar():
        print("El pajaro mira")

# Llamar al método de clase usando el nombre de la clase
piolin= Pajaro('amarillo','canario')
piolin.pintar_negro() #Piolin ahora es negro
print(piolin.color)
Pajaro.poner_huevos(8)
Pajaro.mirar()