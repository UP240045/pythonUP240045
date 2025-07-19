#1
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_cero = [n for n in numeros if n <= 0]

print(negativos_y_cero)

##2
lista_de_lista = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

lista = [num for sublist1 in lista_de_lista for sublist2 in sublist1 for num in sublist2]

print(lista)

#3
resultado = [
    (i, 1, i, i**2, i**3, i**4, i**5)
    for i in range(11)
]

for tupla in resultado:
    print(tupla)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [
    [country[0].upper(), country[0][:3].upper(), country[1].upper()]
    for sublist in countries
    for country in sublist
]

print(new_list)

#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

listad = [
    {'country': country[0].upper(), 'city': country[1].upper()}
    for sublist in countries
    for country in sublist
]

print(listad)

#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

nombres_concatenados = [f"{nombre[0]} {nombre[1]}" for sublist in names for nombre in sublist]

print(nombres_concatenados)

#7
