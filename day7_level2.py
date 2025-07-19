#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

unir = A.union(B)
print("\n",unir)

#2
interseccion = A.intersection(B)
print("\n",interseccion)

#3
print("\n","El conjunto A es subconjunto de B: ",A.issubset(B))

#4
print("\n","El conjunto A y b son disjuntos: ",A.isdisjoint(B))

#5
union_A_B = A.union(B)
union_B_A = B.union(A)

print("\n","Union A con B:", union_A_B)
print("\n","Union B con A:", union_B_A)

#6
difer_simetrica = A.symmetric_difference(B)
print("\n",difer_simetrica)

#7
del A
del B