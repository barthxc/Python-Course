lista = [1,2,3,4]
for numero in lista:
    print(numero)

#usaremos range ahora para recorrer mejor

for numero in range(5): #numero del rango final. empieza en 0
    print(numero)

for numero in range(1,5): #del 1 al 4
    print(numero)

for numero in range(20,31): #del 20 a 30
    print(numero)

for numero in range(20,31,2): #del 20 a 30 de 2 en 2
    print(numero)

#RANGE NO ACEPTA FLOATS

#Metes 100 numeros en una lista

lista= list(range(1,101))

print(lista)



suma_cuadrados = 0
for i in range(1, 16):
    cuadrado = i ** 2
    suma_cuadrados += cuadrado


