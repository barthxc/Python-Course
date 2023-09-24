#Un diccionario: mi_diccionario={'c1':valor1,'c2':valor2,'c3':valor3}
#No puede buscar valores en base a su indice. No importa el orden de los datos
#Se buscan los valores en base a su clave 'c1'
#Sus claves son únicas, no se pueden repetir
diccionario={'c1':'valor1','c2':'valor2'}
print(diccionario)

resultado=diccionario['c1']
print(diccionario['c1'])

cliente={'nombre':'Juan','apellido':'Fuentes','peso':88,'talla':1.76}
consulta=(cliente['talla'])
print(consulta)

#Los diccionarios pueden albergar todo tipo de información
#Por ejemplo otros diccionarios o incluso listas
dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c3']['s2'])


#Ejercicio
dic={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())

#Agregar elementos a un diccionario
dic={1:'a',2:'b'}
print(dic)
dic[3]='c' #Forma de agregar datos al diccionario

print(dic)
#sobre escribir datos
dic[2]=dic[2].upper()
#también funcionaría
dic[2]='B'
print(dic[2])
#Para mostrar solo las claves
print(dic.keys())
#Para mostrar solo los valores
print(dic.values())
#mostrar todo lo que hay en un diccionario
#Si nos fijamos, cuando muestra por pantalla en este método. Lo que vamos son tuplas
print(dic.items())