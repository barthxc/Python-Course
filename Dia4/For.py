nombre = ['Juan','Ana','Carlos','Belen','Fran']
for x in nombre:
    print(f"Hola {x}")

#ITERAR LISTA DE STRNGS
lista = ['a','b','c']
for x in lista:
    numero_letra = lista.index(x)+1
    print(f"Letra {x} en el indice {numero_letra}")

#FOR + condicional
for nombre in nombre:
    if nombre.startswith('F'):
        print(f"{nombre} empieza por F")
    else:
        print(f"{nombre} no empieza por F")



#SUMA DE NUMEROS DE UNA LISTA EN UN FOR
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor= mi_valor+numero
print(mi_valor)



#ITERAR STRINGS con variable
palabra = 'pyton'

for letra in palabra:
    print(letra)
#ITERAR STRINGS dentro del For
for letra in 'python':
    print(letra)


#ITERAR LISTAS DE LISTAS
for a,b in [[1,2],[2,4],[5,6]]:
    print(a)
    print(b)
#ITERAR un diccionario


dic= {'clave1':'a','clave2':'b','clave3':'c'}
#dará como resultado las keys del diccionario
for item in dic:
    print(item)
#dará como resultado los valores del diccionario
for item in dic.values():
    print(item)
#mostrará ambas cosas
for a,b in dic.items():
    print(a,b)
