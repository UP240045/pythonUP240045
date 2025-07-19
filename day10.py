#1
for r in range(11): 
    print("\n",r)

i = 0
while i <= 10:
    print("\n",i)
    i += 1 

#2
for m in range(10, -1, -1):  # Empieza en 10, termina en -1 (no se incluye), va restando de 1 en 1
    print("\n",m)

n = 10
while n >= 0:
    print("\n",n)
    n -= 1

#3
for k in range(1, 8):  # Del 1 al 7
    print("\n",'#' * k)

#4
for v in range(8):  
    for o in range(8):  
        print('#', end=' ') 
    print()

#5
for f in range(11):  
    print("\n",f"{f} x {f} = {f * f}")

#6
lista = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in lista:
    print("\n",item)

#7
for p in range(0, 101):  
    if p % 2 == 0:       
        print("\n",p)

#8
for e in range(0, 101):
    if e % 2 != 0:  
        print("\n",e)