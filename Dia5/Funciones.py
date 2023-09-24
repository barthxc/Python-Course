#para crear una funcion llamada def en minusculas
#def mi_funcion():   y tabulación
#comentario de explicación sobre la función

def mi_funcion(nombre):
    '''
    funcion que llama a un saludo con un nombre
    :param nombre:
    :return:
    '''
    print(f"Hola {nombre}")
mi_funcion('Pablo') #Llamo a mi función

def saludar_persona():
    print(f"Hola")

#RETURN

def multiplicar(numero1,numero2):
    return numero1*numero2

print(multiplicar(2,3))

