import numeros
def preguntar():
    print("Bievenido a nuestra Farmacia ")
    while True:
        print("[P] - Perfumeria \n[F] - Farmacia \n[C] - Cosmética")
        try:
            mi_zona = input("Elija su zona: ").upper()
            ["P","F","C"].index(mi_zona)
        except ValueError:
            print("No es una opción válida.")
        else:
            break
    numeros.decorador(mi_zona)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]").upper()
            ["S","N"].index(otro_turno)
        except ValueError:
            print("Opción incorrecta.")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()