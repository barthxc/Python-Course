#Las tuplas son inmutables, no se pueden cambiar.
#Ocupan menos espacio de memorias por lo tanto son mas rápidos que los diccionarios
#Al no poder modificarse se usan a prueba de daños
#Estructura: 1- mi_tupla= 'perro','gato','rana'
#Estructura: 2- mi_tupla=('raton','cocodrilo','hormiga')
#Pueden contener todo tipo de objeto, incluso varios valores mezclados
#Incluso otro tuple o un diccionario
mi_tupla=(1,2,3,4,'a','b')
print(type(mi_tupla))
print(mi_tupla)
print(mi_tupla[-2]) #funciona como los strings los numeros negativos de buscada por index
#No puedo cambiar los datos de dentro de las tuplas
#ERROR mi_tupla[0]=5

#Anidar
mi_tupla=(1,2,(10,20),4)
print(mi_tupla[2][0])
#Castear tupla
mi_tupla=list(mi_tupla)
print(type(mi_tupla))
mi_tupla=tuple(mi_tupla)

#Asignar el contenido de un tuble a diferentes variables
#También funciona con listas
#Debemos tener los mismo valores que tiene la lista o tubla
t=(1,2,3)
x,y,z=t
print(x,y,z)

#Largo
print(len(t))

#Metodos de tupla
print(t.count(1))#el valor de dentro es el valor que se repote
print(t.index(2))#hay que poner un indice

