texto="Este es el texto de Federico"
resultado=texto
print(resultado)
#upper() - Convierte en mayusculas
print(resultado.upper())
#lower() - Convierte en minusculas
print(resultado.lower())
#split() - Divide el stream
print(resultado.split()) #Parametro dentro es un string que divide los datos. Es el criterio de separación
#join()
a="Aprender"
b="Python"
c="es"
d="genial"
e=" ".join([a,b,c,d]) #Tomará todos los elementos de dentro del parentesis. Necesita un dato de tipo lista []
                      # TOMANDO LA VARIABLE USADA COMO ESPACIO
print(e)
#find()
a.find("e") #Busca un terminado caracter | palabras en el String
            #Si no está el valor que busca, no te da un error. Devuelve -1
#replace()
#Se puede reemplazar varias de esta forma : frase_modificada = frase.replace("difícil", "fácil").replace("mala", "buena")
print(texto.replace("Federico","Pablito")) #Tiene 2 parámetros
                    #1- el parametro que quiero elimintar
                    #2- el que quiero sustituir


