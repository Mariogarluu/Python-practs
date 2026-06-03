import pandas as pd
import numpy as np

# Ejercicio 1: Procesamiento de Logs (Python Puro - Strings y Diccionarios)
# Recibes una lista de cadenas que representan logs del sistema. 
# Formato: "NIVEL: Mensaje de error [fecha]"
# Debes devolver un diccionario anidado donde la clave principal sea la fecha, 
# la subclave sea el NIVEL (ERROR, WARN, INFO), y el valor sea una lista con los mensajes.
# REGLA: Hazlo robusto. Si un log no cumple el formato exacto, ignóralo sin que el programa colapse.
def procesar_logs(logs):
    logs_procesados = {}
    for log in logs:
        try:
            nivel, resto = log.split(': ', 1)
            mensaje, fecha_raw = resto.rsplit(' [', 1)
            fecha = fecha_raw[:-1]
            logs_procesados.setdefault(fecha, {}).setdefault(nivel, []).append(mensaje)
        except ValueError:
            continue
    return logs_procesados

print("--- Ejercicio 1 ---")
logs_sistema = [
    "ERROR: Memoria insuficiente [2026-06-03]",
    "INFO: Inicio de sesión correcto [2026-06-03]",
    "WARN: Latencia alta en red [2026-06-03]",
    "ERROR: Base de datos caída [2026-06-04]",
    "Log corrupto sin formato correcto"
]
print(procesar_logs(logs_sistema))
print()


# Ejercicio 2: Transformación a Tuplas (Python Puro - Listas y Tuplas)
# Recibes una lista de números enteros.
# Debes devolver una lista de tuplas donde cada tupla contenga:
# (número_original, "Par" o "Impar", número_al_cuadrado)
# REGLA: Está prohibido usar bucles tradicionales. Debes resolverlo con una 
# única List Comprehension.
def clasificar_numeros(numeros):
    return [(num, "Par" if num % 2 == 0 else "Impar", num ** 2) for num in numeros]

print("--- Ejercicio 2 ---")
lista_nums = [2, 5, 8, 11]
print(clasificar_numeros(lista_nums))
print()


# Ejercicio 3: Limpieza de Strings Monetarios en Pandas (Data Types)
# Basado en la estructura de tu archivo 'peliculas.csv'.
# Tienes un DataFrame con una columna 'taquilla' que contiene valores en formato string
# como "$700.2M" (Millones) o "$623.4K" (Miles), o valores nulos (NaN).
# 1. Elimina el símbolo '$'.
# 2. Convierte el sufijo 'M' multiplicando por 1,000,000 y 'K' por 1,000.
# 3. Convierte la columna resultante a tipo float.
# 4. Rellena los valores nulos con 0.0.
# Hazlo usando Method Chaining (pista: puedes usar .apply() o funciones de limpieza .str).
def limpiar_taquilla(df):
    return (df.assign(taquilla=lambda x: x['taquilla'].str.replace('$', '', regex=False).str.replace('M', 'e6').str.replace('K', 'e3'))
            .assign(taquilla=lambda x: pd.to_numeric(x['taquilla'], errors='coerce'))
            .assign(taquilla=lambda x: x['taquilla'].fillna(0.0)))

print("--- Ejercicio 3 ---")
df_cine = pd.DataFrame({
    'pelicula': ['Black Panther', 'Texas Rangers', 'Indie Film', 'Avatar'],
    'taquilla': ['$700.2M', '$623.4K', np.nan, '$2000.5M']
})
print(limpiar_taquilla(df_cine))
print("\nTipos de datos:\n", limpiar_taquilla(df_cine).dtypes)
print()


# Ejercicio 4: Extracción de valores máximos por grupo (Pandas - Grouping & Indexing)
# Recibes un DataFrame de películas con 'titulo', 'genero' y 'puntuacion'.
# Debes devolver un DataFrame que contenga ÚNICAMENTE la película con mayor puntuación 
# de cada género.
# REGLA: No puedes usar bucles. 
# (Pista: Investiga el método .idxmax() o combina .sort_values() con .drop_duplicates()).
def top_pelicula_por_genero(df):
    return df.loc[df.groupby('genero')['puntuacion'].idxmax()]

print("--- Ejercicio 4 ---")
df_ranking = pd.DataFrame({
    'titulo': ['Dune', 'Tenet', 'Matrix', 'Joker', 'Batman', 'Gladiator'],
    'genero': ['Ciencia Ficción', 'Ciencia Ficción', 'Ciencia Ficción', 'Drama', 'Acción', 'Acción'],
    'puntuacion': [85, 74, 99, 88, 90, 95]
})
print(top_pelicula_por_genero(df_ranking))
print()