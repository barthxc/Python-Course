#Las listas son de tipo Lista y puede almacenar todo tipo de valores simultaneos.
#Pueden usar métodos de Strings
mi_lista=['a','b','c']
otra_lista=['hola',55,6.1]
print(type(mi_lista))

print(len(mi_lista))
#Indice para listas, igual que Strings
print(mi_lista[0])

print(mi_lista[0:2])

#concatenar listas
print(mi_lista+otra_lista)

#También se pueden sumar para crear una única lista
suma_de_lista=mi_lista+otra_lista
print(suma_de_lista)

#Las listas si pueden mutarse

mi_lista[0]='alfa'
print(mi_lista)

#Agregar datos a la lista
mi_lista.append('g')
print(mi_lista)

#Elimintar elemnto de la lista
mi_lista.pop()#Elimina el ultimo de los elementos. Se debe introducir el indice
mi_lista.append('g')

#Almacenar el elemento eliminado en una variable
eliminado=mi_lista.pop(0)
print(eliminado)

#Métodos de listas-------------------
lista=['g','b','m','c']
lista.sort()
print(lista) #No devuelve la lista ordenada, la lista es cambiada solo en .sort()
#sort() NO DEVUELVE NADA
#nueva_lista = lista.sort() - Esto no funciona
print(lista.sort()) #Me devuelve NONE porque no retorna nada

lista.reverse() #Actual de la misma forma de sort() . Pero pone la lista alreves
#NO RETORNA NADA
print(lista)