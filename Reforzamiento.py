"""Ejercicios de reforzamiento: Primera parte"""

"""Alumma: Karina Belén Pinao Gonzales"""

"""Pregunta 1: Creando una lista de 6 objetos"""

cursos = ["matemáticas", "biología", "estadística", " sociales", "inglés", "química"]

print("Los cursos que lleve en la universidad son: {}".format(cursos))


"""Pregunta 2: Agregando 4 elementos nuevos a la lista creada con list.append(x)"""

cursos.append("biofísica")
cursos.append("farmaco")
cursos.append("histo")
cursos.append("epidemio")

print("Mi lista actualizada es: {}".format(cursos))


"""Pregunta 3: Quitando 2 elementos por valor a la lista anterior con list.remove(x)"""

cursos.remove("biofísica")
cursos.remove("química")

print("Mi lista sin 2 elementos es: {}".format(cursos))


"""Pregunta 4: Invirtiendo el orden de los elementos con list.reverse(x)"""

cursos.reverse()

print("Mi lista invertida es: {}".format(cursos))


"""Pregunta 5: Obteniendo la cantidad total de elementos con len(list(x))"""

print("Mi lista tiene {} elementos".format((len(cursos))))


"""Pregunta 6: Obteniendo el número de veces que se repite un elemento con list.count(x)"""

cursos.append("estadística")

print("La lista con repetición es: {}".format(cursos))

print("El número de veces que se repite 'estadística' es: {}".format(cursos.count("estadística")))


"""Pregunta 7: Borrando un elemento usando su índice con list.pop(x)"""

cursos.pop(0)

print("La lista actualizada sin el primer elemento es: {}".format(cursos))


"""Pregunta 8: Creando una nueva lista vacía y agregando elementos de diferente clase"""

lista2 = []

print(lista2)

# Agregando 3 elementos float:

lista2.append(3.5)
lista2.append(8.2)
lista2.append(9.6)

# Agregando 3 elementos int:

lista2.append(74)
lista2.append(140)
lista2.append(205)

# Agregando 3 elementos string:

lista2.append("Python")
lista2.append("Java")
lista2.append("SQLServer")

print("La nueva lista tiene los siguientes elementos: {}".format(lista2))


"""Pregunta 9: Sumando dos listas creadas anteriormente"""

lista3 = cursos + lista2

print("La nueva lista fusionada es: {}".format(lista3))


"""Pregunta 10: Ordenando los elementos de una lista"""

# Primero creamos las listas en desorden:

lista4 = ["variables", "estructuras", "datos", "elementos"]

print("Mi primera lista sin ordenar es: {}".format(lista4))

lista5 = [105.9, 47, 3.5, 800]

print("Mi segunda lista sin ordenar es: {}".format(lista5))

# Ahora ordenamos las listas

lista4.sort()

print("Mi primera lista ordenada es: {}".format(lista4))

lista5.sort()

print("Mi segunda lista ordenada es: {}".format(lista5))


"""Pregunta 11: Imprimiendo elementos de una lista por índice usando list[i]"""

# Creando lista con 4 elementos float y 2 elementos bools

lista6 = [209.71, 91.03, False, 78.25, True, 4.39]

print("La lista tiene los siguientes elementos: {}".format(lista6))

# Imprimiendo el penúltimo elemento

print("El elemento en la penúltima posición de la lista es: {}".format(lista6[4]))

# Imprimiendo el último elemento

print("El elemento en la última posición de la lista es: {}".format(lista6[5]))


"""Pregunta 12: Reconociendo los tipos de dato usando type(x)"""

print("El tipo de variable de '209.71' es: {}".format(type(209.71)))

print("El tipo de variable de 91.03 es: {}".format(type(91.03)))

print("El tipo de variable de False es: {}".format(type(False)))

print("El tipo de variable de 78.25 es: {}".format(type(78.25)))

print("El tipo de variable de True es: {}".format(type(True)))

print("El tipo de variable de 4.34 es: {}".format(type(4.39)))


"""Pregunta 13: Eliminando elementos de una lista por valor con list.clear(x)"""

lista6.clear()

print("El nuevo estado de la lista6 es: {}".format(lista6))


"""Pregunta 14: Eliminando elementos de una lista por índice"""

# Creando previamente la lista

lista7 = ["Brasil", "Colombia", "Argentina", "Bolivia", "Uruguay"]

print("La lista original es: {}".format(lista7))

# Primera forma: Eliminando elementos por índice usando list.pop(i)

lista7.pop(3)

print("La lista actualizada es: {}".format(lista7))

# Segunda forma: Eliminando elementos por índice usando del list[i]

del lista7[1]

print("la lista nuevamente actualizada es: {}".format(lista7))


"""Pregunta 15: Creando una lista con los 100 primeros enteros"""

# Definimos una función y usamos range


def listado_de_numeros(n):
    numeros = []

    for i in range(1, n + 1):
        numeros.append(i)

    return numeros


listado = listado_de_numeros(100)

print("Los primeros cien números son: {}".format(listado))

# Una segunda forma es usando list(range(m, n)) que empieza en m y acaba en n-1

lista_numeros = list(range(1, 101))

print("Los primeros cien números son: {}".format(lista_numeros))


"""Pregunta 16: Mostrar solo los datos comprendidos entre la posición 10 y 35"""

# Usando la variable 'listado' que creamos en la pregunta 15, definimos las posiciones de inicio y final (n-1)

intervalo = listado[10: 36]

print("Los números del intervalo son: {}".format(intervalo))

# Otra forma es usando la variable 'lista_numeros' que creamos mediante 'list(range())'

intervalo2 = lista_numeros[10:36]

print("Los números del intervalo son: {}".format(intervalo2))


"""Pregunta 17: Creando una lista con los primeros 10 números al cuadrado"""

# Definimos la función y usamos range


def numeros_cuadrados(n):
    cuadrados = []

    for i in range(1, n + 1):
        cuadrados.append(i**2)

    return cuadrados


resultado = numeros_cuadrados(10)

print("Los 10 primeros números al cuadrado son: {}".format(resultado))

# También podemos crear una sintaxis similar para obtener los cubos


def numeros_cubos(n):
    cubos = []

    for i in range(1, n + 1):
        cubos.append(i**3)

    return cubos


resultado2 = numeros_cubos(10)

print("Los 10 primeros números al cubo serían: {}".format(resultado2))


"""Pregunta 18: Creando una lista con números impares, insertar y borrar elementos por índice"""

# Creando una lista con los 15 primeros números impares


def numeros_impares(n):
    impares = []

    for i in range(1, n + 1, 2):
        impares.append(i)

    return impares


resultado3 = numeros_impares(30)

print("Los 15 primeros números impares son: {}".format(resultado3))

# Agregando 3 números flotantes repetidos dentro del rango

resultado3.append(7.0)
resultado3.append(13.0)
resultado3.append(5.0)

print("La lista de números impares actualizada es: {}".format(resultado3))

# Agregando un valor cadena en la posición 3 usando list.insert(i, x)

resultado3.insert(3, "enteros")

print("La lista de números impares con un valor cadena es: {}".format(resultado3))

# Eliminando el valor cadena usando del list[i]

del resultado3[3]

print("La lista actualizada sin el valor cadena es: {}".format(resultado3))

# También se puede obtener los números pares cambiando el índice de inicio


def numeros_pares(n):
    pares = []

    for i in range(2, n + 1, 2):
        pares.append(i)

    return pares


resultado4 = numeros_pares(30)

print("Los 15 primeros números pares serían: {}".format(resultado4))


"""Pregunta 19"""

Nuevalista = [None] * 10

print(Nuevalista)

print("Mi lista tiene {} posiciones".format(len(Nuevalista)))

# Reemplazando valores en las posiciones existentes

Nuevalista[0: 10] = 13, 16, 19, 22, 25, 28, 31, 34, 37, 40

print("Mi lista actualizada es: {}".format(Nuevalista))

print("El lista actualizada tiene {} elementos".format(len(Nuevalista)))

# Obteniendo las posiciones

for posiciones in range(len(Nuevalista)):
    print(posiciones)

# Obteniendo los valores

for i in range(len(Nuevalista)):
    print(Nuevalista[i])

# Sumando los elementos de una lista

suma_de_elementos = 0

for suma in Nuevalista:
    suma_de_elementos += suma

print("La suma de los elementos es: {}".format(suma_de_elementos))

# Otra forma de obtener la suma

suma_de_elementos2 = sum(Nuevalista)
print(suma_de_elementos2)

# Obteniendo el promedio de los elementos

cantidad_de_elementos = len(Nuevalista)

print("Mi lista tiene {} elementos".format(cantidad_de_elementos))

promedio = suma_de_elementos/cantidad_de_elementos

print("La media de los números de la lista es {}".format(promedio))


# Enviar a cursoscerseu6.fisi@unmsm.edu.pe
