#Las funciones generadoras cuidan el espacio en la memoría y se va produciendo y ejecutando funcion poco a poco
#se sustituye return por yield
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista #Ha producido la lista y lo ha devuelto


def mi_generador():
    for x in range(1,5):
        yield x * 10 #Está esperando a ser llamado para que lo muestre



print(mi_funcion()) #Se muestra el 4
print(mi_generador()) #Se muestra el espacio en memoria porque NO lo ha generado / pedido

g= mi_generador()
print(next(g)) #fabrica o haz el siguiente paso en el generador
print(next(g))


def generator2():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x


gene = generator2()

print(next(gene))
print(next(gene))
print(next(gene))


