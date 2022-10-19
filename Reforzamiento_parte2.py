"""Ejercicios de reforzamiento: Segunda parte"""

"""Alumna: Karina Belén Pinao Gonzales"""

"""Diccionarios"""

"""Pregunta 1: Creando un diccionario"""

diccionario1 = {"nombre": "Sara", "edad": "28 años", "salario": 5500, "telefono": 123456}

print("Mi diccionario tiene este contenido: {}".format(diccionario1))


"""Pregunta 2: Convirtiendo el diccionario en una lista"""

list(diccionario1)

print("Mi diccionario convertido a lista es el siguiente: {}".format(list(diccionario1)))


"""Pregunta 3: Agregando un nuevo key al diccionario y mostrar un valor en consola"""

diccionario1["dni"] = 87654321

print("Mi diccionario actualizado es: {}".format(diccionario1))


"""Pregunta 4: Eliminando un key del diccionario incluyendo su valor"""

del diccionario1["edad"]

print("Mi diccionario actualizado sin edad es: {}".format(diccionario1))


"""Pregunta 5: Convirtiendo el diccionario en una lista y mostrar el tipo de datos final"""

list(diccionario1)

print("Mi diccionario actualizado convertido a lista es: {}".format(diccionario1))

valores = list(diccionario1.values())

print("Los valores de mi diccionario convertido a lista son: {}".format(valores))


"""Pregunta 6: Creando un diccionario con los mismos valores sin apuntar a una variable"""

diccionario2 = diccionario1.items()

print("Mi diccionario con los mismos valores es: {}".format(diccionario2))


"""Pregunta 7: Creando un diccionario y borrando un key"""

departamentos = {"Amazonas": 19324, "Ancash": 6732, "Loreto": 7382, "San Martín": 4673, "Ucayali": 4672, "Ica": 9456}

print("El número de adultos mayores vacunados por departamento es: {}".format(departamentos))

# Borrando un departamento usando del

del departamentos["Ancash"]

print("Mi diccionario de departamentos actualizado es: {}".format(departamentos))

# Comprobando si el elemento borrado existe en el diccionario

# Esperando resultado booleano True or False

print("Ancash" in departamentos)

# Usando condicional if

if "Ancash" in departamentos:
    print("El elemento 'Ancash' no fue borrado")
else:
    print("El elemento 'Ancash' fue satisfactoriamente borrado")


"""Pregunta 8: Ingresar un elemento al diccionario"""

departamentos["carrera"] = "patología"

print("Mi diccionario actualizado es: {}".format(departamentos))
