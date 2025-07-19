#1
mi_lista = []

#2
mi_lista2 = [10, "Rodrigo", "Valentina", 322, True, 11]

#3
longitud = len(mi_lista2)
print("\n""La longitud de la lista es: ",longitud)

#4
itemPrim = mi_lista2[0]
itemM = mi_lista2[len(mi_lista2) // 2 - 1]
itemUlt= mi_lista2[-1]

print("\n""Primer item:", itemPrim)
print("\n""Item del medio:", itemM)
print("\n""Ultimo item:", itemUlt)

#5
mixed_data_types = [
    "Rodrigo Duron",
    18,
    1.72,
    "Single"
    "Rinconada Sta. Monica"
]
print("\n",mixed_data_types)

#6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7
print("\n", it_companies)

#8
print("\n",len(it_companies))

#9
primera = it_companies[0]
media = it_companies[len(it_companies) // 2]
ultima = it_companies[-1]

print("\n""Primera empresa:", primera)
print("\n""Empresa del medio:", media)
print("\n""ultima empresa:", ultima)

#10
it_companies2 = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
modificacion = it_companies2.index("Facebook")
it_companies2[modificacion] = "Instagram"
print("\n",it_companies2)

#11
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("Tesla")
print("\n", it_companies)

##12
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
posicion_media = len(it_companies) // 2
it_companies.insert(posicion_media, "Intel")
print("\n",it_companies)

#13
cambioA = it_companies.index('Google')
it_companies[cambioA] = it_companies[cambioA].upper()

print("\n",it_companies)

#14
resultado1 = '#;  '.join(it_companies)

print("\n",resultado1)

#15
empresa = 'Microsoft'
if empresa in it_companies:
    print("\n",f"{empresa} si esta en la lista.")
else:
    print("\n",f"{empresa} no esta en la lista.")

#16
it_companies.sort()

print("\n",it_companies)

#17
it_companies17 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies17.sort()
it_companies17.reverse()

print("\n",it_companies17)

#18
it_companies18 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
primTres = it_companies18[:3]
print("\n",primTres)

#19
it_companies19 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
ultTres = it_companies[-3:]

print("\n",ultTres)

#20
it_companies20 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
num = len(it_companies20)

if num % 2 == 1:
    medio = it_companies20[num // 2]
    print("\n","Empresa del medio:", medio)
else:
    medio = it_companies20[num//2 - 1 : num//2 + 1]
    print("\n","Empresas del medio:", medio)

#21
