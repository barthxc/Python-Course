#Forma dinámica de crear una lista
palabra='python'
lista=[]
lista2=[]

for letra in palabra:
    lista.append(letra)
print(lista)

#COMPRENSION DE LISTAS:

lista2=[letra for letra in palabra]
print(lista2)
lista2=[letra for letra in 'palabra']
print(lista2)


#CON NUMEROS
lista=[n for n in range(0,21,2)]
print(lista)

#Modificar lista

lista=[n/2 for n in range(0,21,2)]
print(lista)

#CONDICIONALES
lista=[n for n in range(0,21,2) if n*2 >10]
print(lista)

#Poner un ELSE?
lista=[n if n*2 >10 else 'no' for n in range(0,21,2)]
#cuando lleva un else se debe poner después del primer N


#práctico- medidas pies   CONVERSOR DE PIES A METROS
pies=[10,20,30,40,50]
metros=[]
metros=[p*3.281 for p in pies]
print(metros)

#Ejercicio 2

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares=[v for v in valores if v%2==0]

#Ejercicio 3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius=[(t-32)*(5/9) for t in temperatura_fahrenheit]