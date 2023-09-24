#Analizador de texto
texto=input("Ingresa un texto a elección: ").lower()
letras=[]
letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())
#Uno no es lo que es por lo que escribe, si no por lo que ha leido
#Frase de Jorge Luis Borges
print("\n")

print("CANTIDAD DE LETRAS")
cantidad_letras1=texto.count(letras[0])
cantidad_letras2=texto.count(letras[1])
cantidad_letras3=texto.count(letras[2])

print(f"Hemos encontrado una letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado una letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado una letra '{letras[2]}' repetida {cantidad_letras3} veces")
print("\n")

print("CANTIDAD DE PALABRAS")
palabras=texto.split() #Esto crea una lista divididad por espacios naturales
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")
print("\n")

print("LETRAS DE INICIO Y DE FIN")
letra_inicio=texto[0]
letra_fin=texto[-1]
print(f"La primera letra es '{letra_inicio}' y la leta final es '{letra_fin}' ")
print("\n")

print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertivo=' '.join(palabras)
print(f"Si ordenamos tu texto alrevés va a decir:\n '{texto_invertivo}'")
print("\n")

print("BUSCANDO LA PALABRA 'PYTHON'")
buscar_python='python' in texto
dic={True:"sí", False:"no"}
print(f"La palabra 'python' {dic[buscar_python]} está en el texto")
