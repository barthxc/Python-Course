def numeros_perfumería():
    for n in range(1,10000):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"


def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"


p = numeros_perfumería()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(zona):

    print("\n + "+"*"* 23)
    print("Su número es:")
    if zona == "P":
        print(next(p))
    elif zona == "F":
        print(next(f))
    else:
        print(next(c))
    print("Espere y será atendido ")
    print("*"* 23 + "\n")
