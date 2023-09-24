from random import *
intentos = 0
numero_usuario=0
numero_secreto=randint(1,100)
print(numero_secreto)
nombre= input("¿Cómo te llamas?: ")
print(f"Hola {nombre}, adivina el numero entre 1  y 100 \n"
      f"Tienes 8 intentos para adivinar")

while intentos < 8:
    numero_usuario=int(input("¿Cuál es el número?: "))
    intentos +=1
    if numero_usuario not in range(1,101):
        print("Tu numero no se encuentra en el rango que va de 1 a 100")
    elif numero_usuario < numero_secreto:
        print("ERROR, tu numero es muy bajo")
    elif numero_usuario > numero_secreto:
        print("ERROR, tu numero es muy alto")
    elif numero_usuario == numero_secreto:
        print(f"FELICIDADES {nombre} adivinaste el numero en {intentos} intentos!")
        break

if numero_usuario != numero_secreto:
    print(f"Has agotado tus intentos!. El numero secreto era {numero_secreto}")
