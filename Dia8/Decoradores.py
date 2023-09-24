#Esta funcion va a decorar cualquier otra funcion
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion

#con el decorador la funcion pasa por la función de decorar saludo
#@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())


mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada('fede')








'''
#podemos guardar una función en una variable
mi_funcion = mayusculas
mi_funcion('python')
#Podemos poner como argumento una funcion EN OTRA FUNCION
def una_funcion(funcion):
    return funcion
'''
