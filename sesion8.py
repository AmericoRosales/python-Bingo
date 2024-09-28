'''
def sumar(a,b):
    global c
    c = 10
    suma = a + b
    return(suma)

print(sumar(20,10))
print(c)



def operaciones(a,b):

    suma = a + b
    return suma
    return a-b

print(operaciones(10,20))

def esPar(n):

    if n%2 == 0:
        return "Es par"
    else:
        return "Es impar"
print(esPar(11))


def operaciones(a,b,c):
    resta = a - b - c
    return resta
    return a - b - c

print(operaciones(20, 5, 10))

def esPar(n):

    if n%2 == 0:
        return "Es par"
    else:
        return "Es impar"
print(esPar(11))
'''


def reto(a,b,c):
    suma = a+b+c

    if suma%2 == 0:
        print("Es par")
    else:
        print("Es impar")

    return suma

print(reto(1,2,3))





