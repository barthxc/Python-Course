#Los métodos de randint está en una libreria llamada Random y no podemos acceder a ellos
#Si no importamos los métodos de dicha libreria
from random import randint  #se ve como comentado, pero está importado
from random import *
#si queremos importarlo todo haremos instalar todo:  from random import *
#NO PODEMOS TENER UN ARCHIVO PY CON EL MISMO NOMBRE QUE RANDOM. En mi caso lo tengo con R mayus
#RADINT = RANDOM+INTEGER
aleatorio=randint(1,50)
print(aleatorio)
#UNIFORM
#uniform me dará un aleatorio float
aleatorio=round(uniform(1,50),1) #solo un numero float para que no te de tantos
print(aleatorio)
#RANDOM
aleatorio=random() #no acepta parámetros, da un resultado aleatorio entre 0 , 1 float
print(aleatorio)

#CHOICE
colores=['azul','rojo','verde','amarillo']
aleatorio=choice(colores) #ME DA UN OPCION ALEATORIA DE UN ITERADOR

#MEZCLA DENTRO DE UN ITERADOR
numeros=list(range(5,50,5)) #creamos una lista de 5 en 5
print(numeros)
shuffle(numeros) #No se puede usar con STRINGS porque son inmutables
print(numeros)