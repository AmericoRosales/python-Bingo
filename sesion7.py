'''
def nombre_funcion(parametros):
    return parametros + " mundo"

nombre_funcion("hola")

en la consola:
hola mundo
'''

def sumar(a,b):
    return print(a + b) #return a + b

sumar(1,2) #print(sumar(1,2))

def sumar_sin():
    a = 1
    b = 2

    return print(a + b)

sumar_sin()

def saludo():
    nombre = input("Escribe tu nombre: ")
    print("Hola", nombre)

saludo()

def sumar_input():
    a = int(input("Ingresa tu primer número: "))
    b = int(input("Ingresa tu segundo número: "))
    print("El resultado es: ", a + b)

sumar_input()

'''
def promedio_notas():
    suma = 0
    for x in range(3):
        nota = int(input("Ingrese la nota: "))
        suma += nota
    promedio = suma/3
    print("El promedio es: ", round(promedio,2))

promedio_notas()
'''

def promedio_notas_condi():
    suma = 0
    for x in range(3):
        nota = int(input("Ingrese la nota: "))
        if not nota > 20:
            suma += nota
        else:
            print("Ingresa una nota correcta")
    if not suma > 60:
        promedio = suma / 3
        print("El promedio es: ", round(promedio, 2))
    else:
        print("Ingrese una nota correcta para un mejor promedio")

promedio_notas_condi()

