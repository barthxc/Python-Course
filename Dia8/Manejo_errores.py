#El try catch de Python     try , except , finally
def suma():
    n1= int(input("numero 1: "))
    n2= int(input("numero 2: "))
    print(n1+n2)
    print("Gracias por sumar " +n1)



try:
    #codigo que queremos probar
    suma()
except TypeError:#codigo a ejecutar si hay un error
    print("Estás intentando concatenar tipos distintos")
except ValueError: #Se puede poner tantos except como quieras/necesitas capturandolos de tipo: TypeError como ejemplo o ValueError
    print("Has ingresado un valor nulo")
else:#OPCIONAL
    print("Hiciste todo bien")
    #codigo que ese ejecuta SI NO HAY UN ERROR
finally:
    print("Eso fue todo.")
    #codigo que se ejecutará de todos modos


def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero"))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")

pedir_numero()



def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("finalizando ejecución")