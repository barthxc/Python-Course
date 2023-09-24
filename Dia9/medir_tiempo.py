'''Hay que revisar el código porque no funciona.'''
import time
import timeit
def prueba_for(numero):
    lista= []
    for num in range(1,numero+1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista=[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador+=1
    return lista

inicio= time.time()
prueba_for(100000)
final = time.time()

print(final-inicio)

print("*******************************************************************")

inicio= time.time()
prueba_while(100000)
final = time.time()

print(final-inicio)


print("USP DE TIMEIT")
#dentro de timeit debemos poner: el nombre de la funcion y lo que hace, guardao por ejemplo en variables distintas además de un integer de repetición

declaracion = '''
prueba_for(10)
'''
mi_setup='''
def prueba_for(numero):
    lista= []
    for num in range(1,numero+1):
        lista.append(num)
    return lista
'''
duracion = timeit.timeit(declaracion,mi_setup, number =100000)
print(duracion)



declaracion2= ''''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista=[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador+=1
    return lista
'''


duracion2 = timeit.timeit(declaracion2,mi_setup2, number =100000)
print(duracion2)
