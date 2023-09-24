def si_cero(*args):
    lista=[]
    contador=0
    for numero in args:
        if numero == 0:
            contador+=1
        if contador==2:
            return False
    return True


#CORRECCION

def ceros_vecinos(*args):
    contador=0
    for num in args:
        if contador +1 == len(args):
            return False
        if args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador+=1
    return False
