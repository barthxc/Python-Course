lista=['a','b','c']

for item in enumerate(lista):
    print(item)

for indice,item in enumerate(lista):
    print(indice,item)

#funciona tambien con rangos

#fuera de loops
#convertir una lista a tupla
lista=['a','b','c']
mi_tupla=list(enumerate(lista))
print(mi_tupla)






lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(nombre,indice)