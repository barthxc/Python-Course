#los conficionales en python es importante tener en cuenta la tabulación y el uso de elif
if 10>9:
    print("Es correcto")

if True:
    print("Es correcto")


x = True

if x:
    print("Es correcto")

if 5==2:
    print("Es correctooooo")
else:
    print("Es falsoooo")


mascota = "perro"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
else:
    print("no se que animal tienes")


edad = 16
calificacion= 9


if edad <18:
    print("Eres menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Suspenso")
else:
    print("Eres adulto")

