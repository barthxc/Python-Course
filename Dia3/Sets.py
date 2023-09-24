#Se puede declarar de 2 maneras
#set(1,2,3,4,,6)
#{1,2,3,4,5,6}
#Para escribir elementos
#Solo admiten elementos únicos, si los metes descargan los duplicados.
#Los elementos no están ordenados de indices, no se puede ordenar u organizarlo
#Elementos inmutables
#No puedes incluir listas o diccionarios
mi_set=set((1,2,3,4,5)) #deben llevar parentesis dentro para llevar 1 único argumento de 5 datos en este ejemplo
print(type(mi_set))
print(mi_set)
#Al no tener un orden interno no se puede buscar por indice
#print(mi_set[0]) esto está mal
#Tampoco podemos cambiar los datos de dentro
#No podemos agregar listas ni diccionarios pero si tuplas
#Los set al ser únicos solo podemos:
#Puedes entrar tuplas porque también son inmutables
mi_set=set((1,2,3,4))
print(len(mi_set))
print(2 in mi_set) #ver si se encuentra un valor dentro de mi set/tuplas/diccionarios/listas
#union de sets
s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)#el método union tiene como parametro lo que vas a unir
print(s3) #ha eliminado el 3 que ha eliminado
s1={1,2,3}
s1.add(4) #agregar datos
s1.remove(3)#eliminar elemento, no puedes eliminar un elemento que no está
s1.discard(3)#descarta un elemento, si no está no se queja
sorteo=s1.pop() #si los parametros están vacio, te elimina un elemento random
print(sorteo)
s1.clear()#limpia el set entero, lo deja vacio
