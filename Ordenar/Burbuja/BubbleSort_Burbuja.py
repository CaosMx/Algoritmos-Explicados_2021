# CaosMX

'''
Ordenado Burbuja:
    Como en un refresco lo que suben son las burbujas, en este método, lo que se realiza es
    enviar a los extremos (izq o der) el valor mayor o menor, según corresponda.

    Se comparan los valores de las posiciones adyacentes (i, i+1) y si es mayor o menor se
    realiza un intercambio de posición [i / i+1], etc hasta que toda la lista se encuentre ordenada:

1) Ejemplo de I -> D
2) Comparar posición i > i+1 ? (i = Posición en la lista)
3) Intercambio o Siguiente posición
4) Repetir hasta n-1 (n = longitud de la lista)

1) Ejemplo de D -> I
2) Comparar posición i < i+1 ? (i = Posición en la lista)
3) Intercambio o Siguiente posición
4) Repetir hasta n-1 (n = longitud de la lista)

'''
lista = [30, 12, 85, 56, 0, 45, 90, 1]
lista2 = [30, 12, 85, 56, 0, 45, 90, 1]
lista3 = [30, 12, 85, 56, 0, 45, 90, 1]
print ("\nLista Original: ", lista, "\n")

# Bubble Sort de I -> D
def BubbleSort (array):
    # Longitud array:
    long = len(array)-1
    #Para recorridos:
    for i in range (0, long):
        print (f'Recorrido #{i+1}')
        #Para comparación y ordenar:
        for j in range (0, long):
            print (f'Comparacion: array[{j}]={array[j]} > array[{j+1}]={array[j+1]} ?')
            if array[j] > array [j+1]:
                #Intercambiamos usando una variable auxiliar o temporal:
                print (f'Si es Mayor, entonces, Intercambiando: {array[j]} X {array[j+1]} ')
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
            else:
                print ("No es Mayor, entonces, Sin intercambio")
    return array

print ("\nUsando Bubble Sort de Menor a Mayor: ")
usandoBs = BubbleSort(lista)
print ("\nUsando Bubble Sort de Menor a Mayor: ", usandoBs)

# Bubble Sort de D -> I
def BubbleSort2 (array):
    # Longitud array:
    long = len(array)-1
    #Para recorridos:
    for i in range (0, long):
        print (f'Recorrido #{i+1}')
        #Para comparación y ordenar:
        for j in range (0, long):
            print (f'Comparacion: array[{j}]={array[j]} < array[{j+1}]={array[j+1]} ?')
            if array[j] < array [j+1]:
                print (f'Si es Menor, entonces, Intercambiando: {array[j]} X {array[j+1]} ')
                #Intercambiamos usando una variable auxiliar o temporal:
                aux = array[j+1]
                array[j+1] = array[j]
                array[j] = aux
            else:
                print ("No es Menor, entonces, Sin intercambio")
    return array

print ("\nUsando Bubble Sort de Mayor a Menor: ")
usandoBs2 = BubbleSort2(lista2)
print ("\nUsando Bubble Sort de Mayor a Menor: ", usandoBs2)

print ("\nLista Original: ", lista3, "\n")
print ("Usando Bubble Sort de Menor a Mayor: ", usandoBs)
print ("Usando Bubble Sort de Mayor a Menor: ", usandoBs2)

# Comprobación
ordenadaPython = sorted(lista3)
print ("Usando Sorted: ", ordenadaPython)