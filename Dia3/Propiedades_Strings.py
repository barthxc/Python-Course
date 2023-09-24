#Propiedades de Strings
    #1- Inmutabilidad
nombre="Carina"
#nombre[0] ="K"  - Esto no funciona
nombre="Karina"
print(nombre)

    #2- Se puede concatenar
n1="Kari"
n2="na"
print(n1+n2)

    #3-Multiplicables
print(n1*10)

    #4- Puede contenre lineas de código
poema= """Mil pequeños peces blancos
como si hirviera 
el color del agua"""
print(poema)
print("agua" in poema) #Pregunta si existe esa cadena en mi variable. Retorna True / False
print("sol" not in poema) #Pregunta si NO existe esa cadena en mi variable. Retorna True / False

#El largo de un String
poema="Hola Mundo!"
print(len(poema))

