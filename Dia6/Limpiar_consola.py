from os import system
#Limpiar la consola en PyCharm y manipular la consola
#system(cls)

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
system('cls') #Limpiar la consola
#Para ello tenemos que ir a RUN / DEBUG / EDIT CONFIGURATION / EMULATE TERMINA IN OUTPUT CONSOLE

print(f"Tu nombre es {nombre} y tu edad {edad}")
