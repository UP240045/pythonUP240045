#1
import random
import string

def random_user_id():
    caracteres = string.ascii_lowercase + string.digits  
    user_id = ''.join(random.choice(caracteres) for _ in range(6))
    return user_id

print(random_user_id())

#2
import random
import string

def user_id_g():
    num_chars = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Cantidad de IDs a generar: "))

    caracteres = string.ascii_letters + string.digits  # mayúsculas + minúsculas + dígitos

    for _ in range(num_ids):
        user_id = ''.join(random.choice(caracteres) for _ in range(num_chars))
        print(user_id)

user_id_g()

#3
import random

def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color())
