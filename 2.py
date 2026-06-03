import pandas as pd

# Ejercicio 1: Limpieza de JSON (Python Puro)
# Recibes una lista de diccionarios, cada uno representando un usuario con 'nombre', 
# 'edad' y 'correo'. Devuelve una lista únicamente con los correos electrónicos de 
# aquellos usuarios que sean mayores de edad (18 o más). 
# Validación: El correo solo se incluye si es un string válido que contenga '@' y '.'.
# Si la lista de entrada está vacía o el formato es incorrecto, devuelve una lista vacía.
def extraer_correos_validos(usuarios):
    if not isinstance(usuarios, list):
        return []

    correos_validos = []
    for usuario in usuarios:
        # Verificar que sea un diccionario y tenga la edad correcta
        if isinstance(usuario, dict) and usuario.get('edad', 0) >= 18:
            correo = usuario.get('correo')
            # Validar que el correo sea un string y contenga '@' y '.'
            if isinstance(correo, str) and '@' in correo and '.' in correo:
                correos_validos.append(correo)

    return correos_validos

print("--- Ejercicio 1 ---")
datos_usuarios = [
    {"nombre": "Ana", "edad": 20, "correo": "ana@email.com"},
    {"nombre": "Luis", "edad": 17, "correo": "luis@email.com"},
    {"nombre": "Carlos", "edad": 25, "correo": "carlos_sin_arroba.com"},
    {"nombre": "Marta", "edad": 30, "correo": "marta@email.es"}
]
print(extraer_correos_validos(datos_usuarios))
print(extraer_correos_validos("datos_corruptos"))
print()


# Ejercicio 2: Agrupación manual (Python Puro)
# Recibes una lista de tuplas con el formato (departamento, nombre_empleado, salario).
# Debes devolver un diccionario donde la clave sea el nombre del departamento y el 
# valor sea el salario promedio de ese departamento, redondeado a 2 decimales.
# Gestiona posibles valores no numéricos en los salarios ignorando esa tupla.
def calcular_promedio_salarial(empleados):
    if not isinstance(empleados, list):
        return {}

    datos_departamento = {}

    for empleado in empleados:
        if isinstance(empleado, tuple) and len(empleado) == 3:
            departamento = empleado[0]
            salario = empleado[2]

            # Verificar que el salario sea un número
            if isinstance(salario, (int, float)):
                if departamento not in datos_departamento:
                    datos_departamento[departamento] = []
                datos_departamento[departamento].append(salario)

    promedios = {}
    for depto, salarios in datos_departamento.items():
        promedios[depto] = round(sum(salarios) / len(salarios), 2)

    return promedios

print("--- Ejercicio 2 ---")
datos_empleados = [
    ("IT", "Mario", 2500.50),
    ("IT", "Laura", 2800.00),
    ("Ventas", "Pedro", 1500.00),
    ("Ventas", "Sofia", "Error_Salario"),
    ("Ventas", "Juan", 1650.75)
]
print(calcular_promedio_salarial(datos_empleados))
print()


# Ejercicio 3: Filtrado y Ordenación con Pandas
# Recibes un DataFrame con las columnas 'producto', 'precio' y 'stock'.
# Devuelve un nuevo DataFrame que contenga solo los productos con stock mayor a 0 
# y cuyo precio sea estrictamente superior a 50.0. 
# El DataFrame resultante debe estar ordenado de mayor a menor precio.
def filtrar_catalogo(df):
    return df[(df['stock'] > 0) & (df['precio'] > 50.0)].sort_values(by='precio', ascending=False)

print("--- Ejercicio 3 ---")
df_catalogo = pd.DataFrame({
    'producto': ['Teclado', 'Ratón', 'Monitor', 'Cable', 'Auriculares'],
    'precio': [120.0, 45.5, 300.0, 15.0, 85.0],
    'stock': [10, 0, 5, 50, 2]
})
print(filtrar_catalogo(df_catalogo))
print()


# Ejercicio 4: Agrupación y Métricas con Pandas
# Recibes un DataFrame de reseñas de videojuegos con 'titulo', 'genero' y 'puntuacion'.
# Utiliza .groupby() para devolver un DataFrame donde el índice sea el 'genero' y 
# tenga dos columnas: la puntuación máxima ('max') y la puntuación media ('mean') 
# de ese género.
def analizar_puntuaciones(df):
    return df.groupby('genero')['puntuacion'].agg(['max', 'mean'])

print("--- Ejercicio 4 ---")
df_juegos = pd.DataFrame({
    'titulo': ['Elden Ring', 'Dark Souls', 'Persona 5', 'Bloodborne', 'Final Fantasy'],
    'genero': ['Soulslike', 'Soulslike', 'JRPG', 'Soulslike', 'JRPG'],
    'puntuacion': [96, 89, 93, 92, 87]
})
print(analizar_puntuaciones(df_juegos))
print()