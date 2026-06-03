import pandas as pd
import numpy as np

# Ejercicio 1: Aplanamiento de JSON y Excepciones (Python Puro)
# Recibes una lista de diccionarios que simula la respuesta de la API de TrackVerse.
# Cada diccionario tiene 'id' y 'perfil'. Dentro de 'perfil' debe haber una lista 'intereses'.
# Devuelve un diccionario donde la clave sea el 'id' y el valor sea la cantidad total de intereses.
# REGLA: Si la clave 'perfil', la clave 'intereses' no existen, o 'intereses' no es una lista, 
# captura el fallo de forma defensiva y asigna 0 intereses a ese 'id'.
def procesar_perfiles_api(respuesta_api):
    resultado = {}
    for usuario in respuesta_api:
        try:
            intereses = usuario['perfil']['intereses']
            if not isinstance(intereses, list):
                raise ValueError
            resultado[usuario['id']] = len(intereses)
        except (KeyError, TypeError, ValueError):
            resultado[usuario['id']] = 0
    return resultado

print("--- Ejercicio 1 ---")
datos_api = [
    {'id': 101, 'perfil': {'intereses': ['Angular', 'Node.js', 'PostgreSQL']}},
    {'id': 102, 'perfil': {'intereses': 'Solo_Frontend'}}, # No es lista
    {'id': 103, 'perfil': {}}, # Faltan intereses
    {'id': 104}, # Falta perfil
    {'id': 105, 'perfil': {'intereses': ['Música Urbana']}}
]
print(procesar_perfiles_api(datos_api))
print()


# Ejercicio 2: Concatenación y Mapeo (Pandas)
# Recibes dos DataFrames del catálogo de hardware (inv_q1 e inv_q2) con 'componente', 'id_cat', 'precio'.
# También recibes un diccionario de mapeo para las categorías.
# 1. Concatena ambos DataFrames verticalmente, ignorando el índice original para no duplicarlo.
# 2. Crea la columna 'categoria' aplicando el diccionario 'mapa_cats' a la columna 'id_cat' usando .map().
# 3. Elimina las filas donde la nueva columna 'categoria' sea NaN (porque el id_cat no estaba en el mapa).
def consolidar_inventario(df_1, df_2, mapa_cats):
    return (pd.concat([df_1, df_2], ignore_index=True)
            .assign(categoria=lambda x: x['id_cat'].map(mapa_cats))
            .dropna(subset=['categoria']))

print("--- Ejercicio 2 ---")
inv_q1 = pd.DataFrame({'componente': ['RTX 4070', 'Ryzen 5'], 'id_cat': [2, 1], 'precio': [600, 200]})
inv_q2 = pd.DataFrame({'componente': ['DDR5 32GB', 'Teclado RGB'], 'id_cat': [3, 99], 'precio': [110, 45]})
mapeo = {1: 'CPU', 2: 'GPU', 3: 'RAM'}
print(consolidar_inventario(inv_q1, inv_q2, mapeo))
print()


# Ejercicio 3: Frecuencias con Series (Pandas + Python Puro)
# Recibes una Serie de Pandas con el registro de jefes derrotados en una sesión.
# 1. Usa el método vectorial .value_counts() para contar cuántas veces se derrotó a cada uno.
# 2. Utiliza una List Comprehension sobre el resultado para devolver una lista en Python puro 
#    con los nombres de los jefes que han sido derrotados estrictamente más de 2 veces.
def jefes_farmeados(serie_bajas):
    return [jefe for jefe, cantidad in serie_bajas.value_counts().items() if cantidad > 2]

print("--- Ejercicio 3 ---")
bajas = pd.Series(['Gundyr', 'Vordt', 'Gundyr', 'Nameless King', 'Gundyr', 'Vordt', 'Vordt'])
print(jefes_farmeados(bajas))
print()


# Ejercicio 4: Agrupación MultiIndex y Aplanamiento de Columnas (Pandas)
# Tienes un DataFrame con cartas de apoyo: 'tipo', 'tier', 'bono'.
# 1. Agrupa por 'tipo' y 'tier'.
# 2. Calcula el 'max' y el 'mean' de la columna 'bono'. (Esto creará columnas anidadas/MultiIndex).
# 3. Para aplanar el MultiIndex resultante, sobrescribe df.columns usando una List Comprehension
#    que una el nivel 0 y el nivel 1 con un guion bajo (ej: 'bono_max', 'bono_mean').
# Devuelve el DataFrame.
def analizar_soporte(df):
    agrupado = df.groupby(['tipo', 'tier'])[['bono']].agg(['max', 'mean'])
    agrupado.columns = [f"{col}_{agg}" for col, agg in agrupado.columns]
    return agrupado

print("--- Ejercicio 4 ---")
df_soporte = pd.DataFrame({
    'tipo': ['Velocidad', 'Resistencia', 'Velocidad', 'Velocidad', 'Resistencia'],
    'tier': ['SSR', 'SR', 'SSR', 'SR', 'SSR'],
    'bono': [20, 10, 15, 8, 18]
})
print(analizar_soporte(df_soporte))
print()