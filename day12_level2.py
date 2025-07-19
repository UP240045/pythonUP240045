#1
import random

def lista_de_hexa(cantidad):
    hexadecimales = '0123456789abcdef'
    lista_colores = []
    
    for _ in range(cantidad):
        color = '#' + ''.join(random.choice(hexadecimales) for _ in range(6))
        lista_colores.append(color)
    
    return lista_colores

colores = lista_de_hexa(5)
print(colores)

#2
import random

def lista_rgb(cantidad):
    lista_colores = []
    for _ in range(cantidad):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = f"rgb({r},{g},{b})"
        lista_colores.append(color)
    return lista_colores


colores = lista_rgb(5)
print(colores)

#3
import random
import string

def generar_color(tipo, cantidad):
    colores = []
    if tipo == 'hexa':
        hexadecimales = '0123456789abcdef'
        for _ in range(cantidad):
            color = '#' + ''.join(random.choice(hexadecimales) for _ in range(6))
            colores.append(color)
    elif tipo == 'rgb':
        for _ in range(cantidad):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = f"rgb({r},{g},{b})"
            colores.append(color)
    else:
        return "Tipo no soportado. Usa 'hexa' o 'rgb'."
    return colores

print(generar_color('hexa', 3))
print(generar_color('hexa', 1))
print(generar_color('rgb', 3))
print(generar_color('rgb', 1))