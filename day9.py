#1
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres lo suficientemente mayor para conducir.")
else:
    años_faltantes = 18 - edad
    print(f"Debes esperar {años_faltantes} año{'s' if años_faltantes > 1 else ''} para poder conducir.")

#2
my_age = 25
your_age = int(input("Ingresa tu edad: "))

if your_age > my_age:
    diferencia = your_age - my_age
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif your_age < my_age:
    diferencia = my_age - your_age
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")

#3
a = float(input("Ingresa el primer número (a): "))
b = float(input("Ingresa el segundo número (b): "))

if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")
