#!
puntaje = int(input("Ingresa la calificación del estudiante (0-100): "))

if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje <= 79:
    print("Calificación: B")
elif 60 <= puntaje <= 69:
    print("Calificación: C")
elif 50 <= puntaje <= 59:
    print("Calificación: D")
elif 0 <= puntaje <= 49:
    print("Calificación: F")
else:
    print("Puntaje inválido. Debe estar entre 0 y 100.")

#2
mes = input("Ingresa el nombre de un mes: ").strip().capitalize()

if mes in ["Septiembre", "Octubre", "Noviembre"]:
    print("La estación es Otoño.")
elif mes in ["Diciembre", "Enero", "Febrero"]:
    print("La estación es Invierno.")
elif mes in ["Marzo", "Abril", "Mayo"]:
    print("La estación es Primavera.")
elif mes in ["Junio", "Julio", "Agosto"]:
    print("La estación es Verano.")
else:
    print("Mes inválido. Asegúrate de escribir el mes correctamente.")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']

nueva_fruta = input("Ingresa una fruta: ").strip().lower()

if nueva_fruta in fruits:
    print("Esa fruta ya existe en la lista.")
else:
    fruits.append(nueva_fruta)
    print("Fruta agregada. Lista actualizada:")
    print(fruits)

