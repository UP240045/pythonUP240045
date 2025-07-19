#1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    longitud = len(skills)
    medio = longitud // 2
    if longitud % 2 == 0:
        print("Habilidades del medio:", skills[medio - 1], "y", skills[medio])
    else:
        print("Habilidad del medio:", skills[medio])

if 'skills' in person:
    tiene_python = 'Python' in person['skills']
    print("¿Tiene Python?:", tiene_python)

if 'skills' in person:
    habilidades = set(person['skills'])

    if habilidades == {'JavaScript', 'React'}:
        print('Es un desarrollador Frontend')
    elif {'Node', 'Python', 'MongoDB'}.issubset(habilidades):
        print('Es un desarrollador Backend')
    elif {'React', 'Node', 'MongoDB'}.issubset(habilidades):
        print('Es un desarrollador Fullstack')
    else:
        print('Título desconocido')

if person.get('is_marred') and person.get('country') == 'Finlandia':
    nombre_completo = person['first_name'] + " " + person['last_name']
    print(f"{nombre_completo} vive en Finlandia. Está casado.")
