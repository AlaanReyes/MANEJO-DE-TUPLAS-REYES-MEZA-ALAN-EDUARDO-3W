print("Welcome to Project 1!")  # BIENVENIDA AL PROGRAMADOR 
print(" ")  # ESPACIO

print("REYES MEZA ALAN EDUARDO : PRACTICAS TUPLAS   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# Crear tupla
thistuple = ("apple", "banana", "cherry")
print("Tupla original:", thistuple)

# Tupla con miembros duplicados 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("Tupla con duplicados:", thistuple)

# Contando miembros de la tupla
print("Número de elementos en la tupla:", len(thistuple))

# Notar la diferencia de cuando SÍ es tupla y cuando NO
thistuple = ("apple",)
print("Tipo de thistuple (un elemento):", type(thistuple))

# NOT a tuple
thistuple = ("apple")
print("Tipo de thistuple (no es tupla):", type(thistuple))

# Asignando tuplas a variables 
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Combinando tipos de datos en mis tuplas
mixed_tuple = ("abc", 34, True, 40, "male")
print("Tupla con diferentes tipos de datos:", mixed_tuple)

# Tipo de datos de una tupla
mytuple = ("apple", "banana", "cherry")
print("Tipo de mytuple:", type(mytuple))

# Utilizando el método tuple para crear una tupla
thistuple = tuple(("apple", "banana", "cherry"))
print("Tupla creada con el método tuple:", thistuple)

# Accediendo a elementos de una tupla
print("Primer elemento de thistuple:", thistuple[0])
print("Último elemento de thistuple:", thistuple[-1])

# Slicing de tuplas
print("Elementos de índice 1 a 3 (exclusivo):", thistuple[1:3])

# Intentando modificar una tupla (esto generará un error)
try:
    thistuple[1] = "orange"  # Esto lanzará un TypeError
except TypeError as e:
    print("Error al intentar modificar la tupla:", e)

# Concatenando tuplas
tuple_a = ("apple", "banana")
tuple_b = ("cherry", "date")
combined_tuple = tuple_a + tuple_b
print("Tupla combinada:", combined_tuple)

# Replicando tuplas
replicated_tuple = tuple_a * 3
print("Tupla replicada 3 veces:", replicated_tuple)

# Verificando si un elemento está en la tupla
print("¿'banana' está en la tupla?", "banana" in tuple_a)

# Contando elementos en la tupla
print("Número de veces que 'apple' aparece en tuple_a:", tuple_a.count("apple"))

# Obteniendo el índice de un elemento
print("Índice de 'banana' en tuple_a:", tuple_a.index("banana"))

# Desempaquetando tuplas
fruit1, fruit2 = tuple_a
print("Desempaquetando tuple_a: fruit1 =", fruit1, ", fruit2 =", fruit2)

# Crear una tupla de un rango
range_tuple = tuple(range(5))
print("Tupla de un rango (0 a 4):", range_tuple)

# Tupla anidada
nested_tuple = (("apple", "banana"), (1, 2, 3))
print("Tupla anidada:", nested_tuple)
print("Accediendo a un elemento de la tupla anidada:", nested_tuple[0][1])  # Accede a 'banana'





