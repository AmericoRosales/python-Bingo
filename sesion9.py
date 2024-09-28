import random
import time


#Crear una lista de números enteros
def listaNum(start, end):
    lista = []

    for x in range(start, end+1):
        lista.append(x)

    return lista

#Creamos la cartillas
def cartillas(inicio, fin, cantidad):

    lista = listaNum(inicio, fin)
    listaNueva = []

    for x in range(cantidad):
        a = random.randint(0, len(lista)-1)     #Elige un indice al azar de la lista
        n = lista[a]                               #Escoge el elemento de la lista correspondiente a dicho índice
        listaNueva.append(n)                       #Añade el número escogido a la nueva lista
        lista.pop(a)                               #Elimina dicho elemento de la lista
    print(listaNueva)

def Bolillas():

    lista = listaNum(1,75) #Creamos una lista con números del 1 al 75

    while len(lista)>0: #mientras la lista tenga números
        a = random.randint(0, len(lista) -1) #Escogemos un indice al azar
        n = lista[a]    #Verificamos el numero correspondiente al indice
        print(n, end=" ")   #Imprimir dicho número
        lista.pop(a)    #Eliminamos el indice de la lista original
        print()     #Imprimir un espacio
        time.sleep(5)   #Tiempo de espera de 5 segundos

cartillas(1,15,5)
cartillas(16,30,5)
cartillas(31,45,4)
cartillas(46,60,5)
cartillas(61,75,5)

Bolillas()
