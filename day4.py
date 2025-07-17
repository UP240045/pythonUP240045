##1
palabra1 = "Thirty"
palabra2 = "Days"
palabra3 = "Of"
palabra4 = "Python"
espacio = " "

palabracompleta = palabra1 +espacio+ palabra2 +espacio +palabra3 +espacio+ palabra4
print("\n","First Word: ",palabracompleta)
##2
word1 = "Coding"
word2 = "For"
word3 = "All"
space = ""

word = word1+space+word2+space+word3
print("\n","Second Word: ",word)
##3
Company = "Coding For All"
##4
print("\n",Company)

##5
print("\n","The lenght of the word is: ",len(Company))
##6
uppercase_text = Company.upper()
print("\n","The phrase in uppercase is: ",uppercase_text)
##7
lowercase_text = Company.lower()
print("\n","The phrase in lowercase is: ",lowercase_text)
##8
capitalize_text = Company.capitalize()
title_text = Company.title()
swapcase_text = Company.swapcase()
print("\n","The capitalize text is: ",capitalize_text)
print("\n","The title text is: ",title_text)
print("\n","The swapcase is: ",swapcase_text)
##9
fsi = Company.find(" ")
sliced_text = Company[fsi + 1:]
print("\n","The sliced text is: ",sliced_text)
##10
if "Coding" in Company:
    print("\n","The word 'Coding' is in the phrase ")
else:
    print("\n","The word 'Coding' is not in the phrase")
##11
print("\n",Company.replace('Coding','Python'))
##12
NewText = "Python For Everyone"
print("\n",NewText.replace('Python For Everyone','Python For All'))
##13
print("\n",Company.split())
##14
TextEx14 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("\n",TextEx14.split(', '))
##15
print("\n","The character at index 0 is: ",Company[0])
##16
last_index = len(Company) - 1
print("\n","The last index is: ",last_index)
##17
print("\n","The character at index 10 is: ",Company[10])
##18
def crear_acronimo(frase):
    palabras = frase.split()
    acronimo = ''.join([p[0].upper() for p in palabras])
    return acronimo
nombre = "Python For Everyone"
print("Acronimo: ", crear_acronimo(nombre)) 
#19
def crear_acronimo(frase):
    palabras = frase.split()
    acronimo = ''.join([palabra[0].upper() for palabra in palabras])
    return acronimo
nombre = "Coding For All"
print("Acronimo: ", crear_acronimo(nombre)) 
#20
frase = "Coding for All"
posicion = frase.index("C")
print("La letra C esta en la posicion: ",posicion)
#21
frase = "Coding For All"
posicion2 = frase.index("F")
print("La letra F esta en la posicion: ",posicion2)
#22
frase2 = "Coding For All People"
posicion3 = frase.rfind("l")
print("Esta en la posicion: ",posicion3)
#23
frase3 = "You cannot end a sentence with because because because is a conjunction"
posicion4 = frase3.index("because")
print("La palabra because esta en la posicion: ", posicion4)
#24
frase3 = "You cannot end a sentence with because because because is a conjunction"
posicion5 = frase3.rindex("because")
print(posicion5)
#25
frase3 = "You cannot end a sentence with because because because is a conjunction"
inicio = frase3.find("because because because")
final = inicio + len("because because because")
resultado = frase3[inicio:final]
print(resultado)
#26
frase3 = "You cannot end a sentence with because because because is a conjunction"
posicion6 = frase.find("because")
print(posicion6)
#27
frase3 = "You cannot end a sentence with because because because is a conjunction"
inicio1 = frase3.find("because because because")
final1 = inicio1+len("because because because")
resultadoF = frase3[inicio1:final1]
print(resultadoF)
#28
frase28 = "Coding For All"
resultado28 = frase28.startswith("Coding")
print(resultado28)
#29
frase29 = "Coding For All"
resultado29 = frase29.endswith("Coding")
print(resultado29)
#30
frase30 = '   Coding For All      '
resultado30 = frase30.strip()
print(f"'{resultado30}'")
#31
print("30DaysOfPython".isidentifier())        
print("thirty_days_of_python".isidentifier()) 
#32
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado32 = "# ".join(librerias)
print(resultado32)
#33
linea = "I am enjoying this challenge.\nI just wonder what is next."
print(linea)
#34
linea2 = texto = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(linea2)
#35
radius = 10
area = 3.14 * radius ** 2

mensaje35 = "The area of a circle with radius {} is {} meters square.".format(radius, area)
print(mensaje35)
#36
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

