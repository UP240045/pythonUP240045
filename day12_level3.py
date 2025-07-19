#1
import random

def shuffle_list(lista):
    lista_copiada = lista[:]          
    random.shuffle(lista_copiada)     
    return lista_copiada

original = [1, 2, 3, 4, 5]
mezclada = shuffle_list(original)
print("Original:", original)
print("Mezclada:", mezclada)

#2
import random

def numeros_unicos():
    return random.sample(range(10), 7)

numeros = numeros_unicos()
print(numeros)
