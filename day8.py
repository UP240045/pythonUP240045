#1
dog = {}

#2
dog['name'] = 'BamBam'
dog['color'] = 'Atigrado'
dog['breed'] = 'BullDog Frances'
dog['legs'] = 4
dog['age'] = 3

print("\n",dog)

#3
student = {
    'first_name': 'Valentina',
    'last_name': 'Rodriguez',
    'gender': 'Femenino',
    'age': 19,
    'marital_status': 'Casada',
    'skills': ['AutoCad', 'Dibujo', 'Construcciom'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': 'Av. Siglo XXI'
}
print("\n",student)

#4
print("\n",len(student))

#5
skills = student.get('skills')

print("\n","Skills:", skills)
print("\n","Tipo de dato:", type(skills))

if isinstance(skills, list):
    print("\n","Es una lista.")
else:
    print("\n","No es una lista.")

#6
student['skills'].append('Diseño')

student['skills'].extend(['Circuitos', 'Interiores'])

print("\n",student['skills'])

#7
keys_list = list(student.keys())

print("\n",keys_list)

#8
values_list = list(student.values())

print("\n",values_list)

#9
items_list = list(student.items())

print("\n",items_list)

#10
del student['address']

print("\n",student)

#11
del student