#Método index
    #1-Conoces el índice de un caracter - variable.index("char")
    #2-Conocer qué caracter hay en un índice - variable[3]
mi_texto="Esta es una prueba"
                        #-1 sería la letra A de prueba
resultado=mi_texto[-4]
print(resultado)
    #Format puede tener 3 parámetro
        #1- La letra o palabra variables variable.index("prueba")  el resultado será el primer indice de la letra P
            #Tiene keysensitive, distingue de mayúsculas. Hace un rastreo de izquierda - derecha
        #2- Segundo parámetro empieza a buscar desde el indez que pongas variable.index("a",5) busca la '2' a partir del indice 5
        #3- Tercer parámetro es indicando el final
print(mi_texto.index("prueba"))
        #El método rindex() hace lo mismo pero buscando de derecha a izquierda
print(mi_texto.rindex("prueba"))


