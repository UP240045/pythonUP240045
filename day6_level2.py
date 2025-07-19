#1
hermanos = ("Alfredo","Cathy","Angelito","Rodrigo")
padres = ("Alfredo","Marisela")

familia = hermanos + padres
hermanos_unpacked = familia[:4]
padres_unpacked = familia[4:]

print("Siblings:", hermanos_unpacked)
print("Parents:", padres_unpacked)

#2
frutas = ("Sandia","Platano","Cereza")
vegetales = ("Cebolla","Zanahoria","Lechuga")
ProdAnimal = ("Queso","Huevo","Miel")

food_stuff_tp = frutas + vegetales + ProdAnimal
print("\n",food_stuff_tp)

#3
food_stuff_tp1 = ("Sandia","Platano","Cereza","Cebolla","Zanahoria","Lechuga","Queso","Huevo","Miel")
food_stuff_lt = list(food_stuff_tp1)

print("\n",food_stuff_lt)

#4
n = len(food_stuff_tp1)
if n % 2 == 1:
    medio = food_stuff_tp1[n // 2]
else:
    medio = food_stuff_tp1[n//2 - 1 : n//2 + 1]

print("\n","Elementos del medio:", medio)

#5
food_stuff_lt1 = list(food_stuff_tp1)

primeros_tres = food_stuff_lt1[:3]

ultimos_tres = food_stuff_lt1[-3:]

print("\n","Primeros 3 elementos:", primeros_tres)
print("\n","Ultimos 3 elementos:", ultimos_tres)

#6
del food_stuff_tp1

#7
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("\n","Estonia esta en la tupla: ",'Estonia' in nordic_countries)
print("\n","Islandia esta en la tupla: ",'Iceland' in nordic_countries)