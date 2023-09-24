def ordenacion(palabra):
#pasar la palabra en una lista, ordenarla y eliminar sus valores repetidos
    lista=[]
    for letra in palabra:
        if letra not in lista:
            lista.appen(letra)
    lista.sort()
    return lista

#NO SE SI FUNCIONA: CORRECCION ABAJO
#CORRECCION USANDO SET PARA QUE NO SE GUARDEN VALORES ÚNICOS
def letras_unicas(palabra):
    mi_set=set()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista=list(mi_set)
    mi_lista.sort()
    return mi_lista

