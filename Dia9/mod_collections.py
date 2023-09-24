from collections import Counter,defaultdict,namedtuple
#Con counter podemos mostrar todos los valores repeditos
numeros = [8,6,9,5,4,5,5,5,5,5,8,8,5,4,4]
print(Counter(numeros))#Muestra un tipo de diccionario donde aparece el valor y la cantidad repetida
print(Counter('mississippi')) #Hace lo mismo con letras
frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

serie =  Counter([1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,5,5,5,5,5,5,4,3,2,1])
print(serie.most_common(1)) #Mostrará los valores ordenados por mas repetidos
#si ponemos un numero de argumentos, mostramos los mas repetidos

print(list(serie))


#Con defaultdict podemos averiguar si hay un dato basada en el valor. Si no lo está crea un valor por defecto como 'nada'
mi_dic = {'uno':'verde', 'dos':'azul','tres':'rojo'}
print(mi_dic['dos'])


mi_dic2 = defaultdict(lambda:'nada')
mi_dic2['uno'] = 'verde'
print(mi_dic2['dos'])
print(mi_dic2)

#NamedTuple podemos acceder a valores de la tupla a través de un nombre

Persona = namedtuple('Persona',['nombre','altura','peso'])#definimos nombres para datos de la tupla
ariel = Persona('Ariel',1.76,79)
mi_tupla = (500,60,14)
print(mi_tupla[1])
print(ariel.altura)
print(ariel[1])

