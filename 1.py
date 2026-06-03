# Ejercicio 1: Validación de Cadenas
# Crea una función validar_usuario que reciba un string. Debe devolver True solo si 
# cumple todas estas condiciones: longitud entre 5 y 15 caracteres, es alfanumérico, 
# y el primer carácter es obligatoriamente una letra.
def validar_usuario(usuario):
    if type(usuario) is not str:
        return False
    if not (5 <= len(usuario) <= 15):
        return False
    if not usuario.isalnum():
        return False
    if not usuario[0].isalpha():
        return False
    return True

print("--- Ejercicio 1 ---")
print(validar_usuario("Mario2026"))
print(validar_usuario("123Mario"))
print(validar_usuario("Mar@io"))
print(validar_usuario(["Mario2026"]))
print()


# Ejercicio 2: Bucles y Lógica Matemática
# Crea una función filtrar_primos que reciba una lista de números enteros. Debe 
# devolver una nueva lista que contenga únicamente los números primos de la lista original. 
# No puedes usar librerías externas.
def filtrar_primos(numeros):
    if type(numeros) is not list:
        return []
    primos = []
    for num in numeros:
        if type(num) is not int or num <= 1:
            continue
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

print("--- Ejercicio 2 ---")
print(filtrar_primos([2, 3, 4, 5, 10, 13, -5, "texto"]))
print(filtrar_primos("2, 3, 5"))
print()


# Ejercicio 3: Frecuencia con Diccionarios
# Crea una función contar_caracteres que reciba un string (por ejemplo, un log del sistema) 
# y devuelva un diccionario donde las claves sean los caracteres (en minúsculas, ignorando 
# espacios) y los valores sean la cantidad de veces que aparecen.
def contar_caracteres(texto):
    if type(texto) is not str:
        return {}
    frecuencias = {}
    for char in texto.lower():
        if char != ' ':
            frecuencias[char] = frecuencias.get(char, 0) + 1
    return frecuencias

print("--- Ejercicio 3 ---")
print(contar_caracteres("Hola Chiqui"))
print(contar_caracteres(12345))
print()


# Ejercicio 4: Ordenación de Tuplas
# Tienes una lista de tuplas que representan equipamiento: (nombre_arma, daño, peso). 
# Crea una función ordenar_build que ordene esta lista de mayor a menor daño. Si dos 
# armas tienen el mismo daño, debe ir primero la que tenga menor peso.
def ordenar_build(equipamiento):
    if type(equipamiento) is not list:
        return []
    return sorted(equipamiento, key=lambda x: (-x[1], x[2]))

print("--- Ejercicio 4 ---")
armas = [("Espada Larga", 50, 10), ("Daga Rápida", 30, 2), ("Hacha Pesada", 50, 15)]
print(ordenar_build(armas))
print()


# Ejercicio 5: List Comprehensions
# Usando una única línea de código (list comprehension), genera una lista que contenga 
# los cuadrados de todos los números pares del 1 al 50, pero solo incluye aquellos cuadrados 
# que sean divisibles por 3. Asigna el resultado a una variable cuadrados_especiales.
cuadrados_especiales = [x**2 for x in range(2, 51, 2) if (x**2) % 3 == 0]

print("--- Ejercicio 5 ---")
print(cuadrados_especiales)
print()


# Ejercicio 6: Manejo de Excepciones
# Crea una función calcular_rendimiento que reciba dos listas: fps_registrados y uso_cpu. 
# La función debe devolver una lista con el resultado de dividir cada valor de FPS por su 
# correspondiente uso de CPU. Si hay un error de división por cero o tipos de datos incorrectos 
# (letras mezcladas), la función debe insertar el string "ERROR" en esa posición de la lista 
# resultante en lugar de detener la ejecución.
def calcular_rendimiento(fps_registrados, uso_cpu):
    if type(fps_registrados) is not list or type(uso_cpu) is not list:
        return []
    resultados = []
    longitud = min(len(fps_registrados), len(uso_cpu))
    for i in range(longitud):
        try:
            resultados.append(fps_registrados[i] / uso_cpu[i])
        except (ZeroDivisionError, TypeError):
            resultados.append("ERROR")
    return resultados

print("--- Ejercicio 6 ---")
print(calcular_rendimiento([60, 120, 144, "drop"], [30, 0, 50, 20]))
print()


# Ejercicio 7: Diccionarios Anidados
# Tienes un diccionario de usuarios de una app social donde la clave es el nombre y el 
# valor es una lista de puntuaciones otorgadas a diferentes obras. Crea una función 
# calcular_medias que reciba este diccionario y devuelva uno nuevo donde la clave sea el 
# usuario y el valor sea su nota media redondeada a dos decimales.
def calcular_medias(puntuaciones_usuarios):
    if type(puntuaciones_usuarios) is not dict:
        return {}
    medias = {}
    for usuario, notas in puntuaciones_usuarios.items():
        if type(notas) is not list or len(notas) == 0:
            medias[usuario] = 0.0
            continue
        try:
            medias[usuario] = round(sum(notas) / len(notas), 2)
        except TypeError:
            medias[usuario] = "ERROR"
    return medias

print("--- Ejercicio 7 ---")
print(calcular_medias({"UserA": [10, 9, 8], "UserB": [], "UserC": [10, "A"]}))
print()


# Ejercicio 8: Algoritmos Básicos
# Crea una función es_palindromo que determine si una frase leída de izquierda a derecha 
# es igual que de derecha a izquierda. Debe ignorar espacios, signos de puntuación básicos 
# (comas y puntos) y no ser sensible a mayúsculas/minúsculas.
def es_palindromo(frase):
    if type(frase) is not str:
        return False
    limpia = frase.lower().replace(" ", "").replace(",", "").replace(".", "")
    return limpia == limpia[::-1]

print("--- Ejercicio 8 ---")
print(es_palindromo("Anita lava la tina."))
print(es_palindromo("TrackVerse"))
print(es_palindromo(1001))