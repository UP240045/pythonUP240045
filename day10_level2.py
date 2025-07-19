#1
total = 0
for x in range(101): 
    total += x

print("La suma de los numeros del 0 al 100 es:", total)

#2
sum_even = 0
sum_odd = 0

for z in range(101):
    if z % 2 == 0:
        sum_even += z
    else:
        sum_odd += z

print("Suma de numeros pares:", sum_even)
print("Suma de numeros impares:", sum_odd)
