nombre = 'Rodrigo'
apellido = 'Duron'
nombreCompleto = nombre, apellido
Pais = 'Mexico'
Ciudad = 'Aguascalientes'
Edad = 18
Año = 2025
Casado = False
Es_Verdadero = True
Luz_Encendida = True

nombre,apellido,Ciudad,Edad = 'Rodrigo','Duron','Aguascalientes','18 años'
print(nombre,apellido,Ciudad,Edad)
print('Nombre:',nombre)
print('Apellido:',apellido)
print('Ciudad:',Ciudad)
print('Edad:',Edad)



print(type(nombre))
print(type(apellido))
print(type(nombreCompleto))
print(type(Pais))
print(type(Ciudad))
print(type(Edad))
print(type(Año))
print(type(Casado))
print(type(Es_Verdadero))
print(type(Luz_Encendida))

print('Longitud de Nombre:',len(nombre))
print('Longitud de Apellido:',len(apellido))

print(f"La longitud del nombre es de: {len(nombre)} caracteres y la longitud del apellido es de: {len(apellido)} caracteres")

num_1=5
num_2=4

Total=num_1+num_2
print("El total de la suma es: ",Total)
diff = num_1-num_2
print("La diferencia de la resta es: ",diff)
producto =num_1*num_2
print("El producto de la multiplicacion es: ",producto)
Division=num_1/num_2
print("El resultado de la division es: ",Division)
Residuo=num_1%num_2
print("El residuo es: ",Residuo)
Exp= num_1**num_2
print("El total del numero elevado es: ",Exp)
DivisionPiso=num_1//num_2
print("La division de piso es de: ",DivisionPiso)

radio=30
pi=3.14

AreaCirculo= pi*radio**2
Circunferencia_Circulo=pi*radio*2

print("El area del circulo es: ",AreaCirculo)
print("La circunferencia del circulo es: ",Circunferencia_Circulo)

RadioUsuario=float(input("Introduzca el radio del circulo: "))
Area=pi*(RadioUsuario**2)
print("El area del circulo es: ",Area)

nombreInput = (input("Ingresa tu nombre: "))
apellidoInput = (input("Ingresa tu apellido: "))
paisInput = (input("Ingresa tu país: "))
edadInput = int(input("Ingresa tu edad: "))

print(f"Tu nombre es {nombreInput}")
print(f"Tu apellido es: {apellidoInput}")
print(f"Tu país es: {paisInput}")
print(f"Tu edad es: {edadInput} años")

print("\nPython reserved keywords:")
help('keywords')