#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
len_list = len(age)
len_set = len(age_set)

print("\n","Longitud de la lista: ", len_list)
print("\n","Longitud del set: ", len_set)
if len_list > len_set:
    print("\n","La lista es mas grande (tiene duplicados).")
elif len_list < len_set:
    print("\n","El set es mas grande (esto no suele pasar).")
else:
    print("\n","La lista y el set tienen el mismo tamaño.")

#3
sentencia = "I am a teacher and I love to inspire and teach people."

sentencia_clean = sentencia.replace('.', '')
palabras = sentencia_clean.split()
palabras_unicas = set(palabras)
num_palabras_unicas = len(palabras_unicas)

print("\n","Palabras unicas:", palabras_unicas)
print("\n","Numero de palabras unicas:", num_palabras_unicas)

