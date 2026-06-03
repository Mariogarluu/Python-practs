import pandas as pd
import numpy as np

# Ejercicio 1: Lógica, Diccionarios y Excepciones (Python Puro)
# Recibes una lista de diccionarios que representan el inventario y ventas de componentes de PC.
# Cada diccionario tiene 'id', 'categoria', 'precio', 'cantidad_vendida'.
# Calcula el total de ingresos (precio * cantidad_vendida) por categoría.
# REGLAS: 
# 1. Ignora los diccionarios que no tengan la clave 'precio' o 'cantidad_vendida'.
# 2. Ignora los registros donde los valores no sean numéricos (maneja las excepciones).
# 3. Devuelve un diccionario con el formato: {'categoria': ingreso_total_acumulado_redondeado_a_2_decimales}
def calcular_ingresos_por_categoria(ventas):
    ingresos = {}
    for venta in ventas:
        if 'precio' in venta and 'cantidad_vendida' in venta:
            try:
                precio = float(venta['precio'])
                cantidad = int(venta['cantidad_vendida'])
                categoria = venta['categoria']
                ingresos[categoria] = ingresos.get(categoria, 0.0) + (precio * cantidad)
            except (ValueError, TypeError):
                continue
    return {k: round(v, 2) for k, v in ingresos.items()}

print("--- Ejercicio 1 ---")
datos_ventas = [
    {'id': 1, 'categoria': 'GPU', 'precio': 850.50, 'cantidad_vendida': 2},
    {'id': 2, 'categoria': 'CPU', 'precio': 400.00, 'cantidad_vendida': "Error"},
    {'id': 3, 'categoria': 'RAM', 'precio': 120.00, 'cantidad_vendida': 5},
    {'id': 4, 'categoria': 'GPU', 'precio': 1200.00, 'cantidad_vendida': 1},
    {'id': 5, 'categoria': 'Placa Base'} # Faltan datos
]
print(calcular_ingresos_por_categoria(datos_ventas))
print()


# Ejercicio 2: Limpieza e Indexación Avanzada (Pandas)
# Tienes un DataFrame con el historial de jugadores de un título de rol: 'jugador', 'nivel', 'horas_juego', 'rango'.
# 1. Rellena las 'horas_juego' nulas (NaN) con el promedio (mean) de esa columna.
# 2. Elimina cualquier fila donde el 'rango' sea nulo (NaN).
# 3. Usa EXCLUSIVAMENTE .loc para filtrar y devolver solo los jugadores con 'nivel' mayor o igual a 100 
#    y que tengan estrictamente más de 50 'horas_juego'.
def filtrar_veteranos(df):
    return (df.dropna(subset=['rango'])
            .assign(horas_juego=lambda x: x['horas_juego'].fillna(x['horas_juego'].mean()))
            .loc[lambda x: (x['nivel'] >= 100) & (x['horas_juego'] > 50)])

print("--- Ejercicio 2 ---")
df_jugadores = pd.DataFrame({
    'jugador': ['Tarnished1', 'GutsBuild', 'AshenOne', 'CarianKnight', 'LetMeSolo'],
    'nivel': [150, 120, 90, 110, 200],
    'horas_juego': [120.0, np.nan, 45.0, np.nan, 300.0],
    'rango': ['Oro', 'Plata', 'Bronce', np.nan, 'Diamante']
})
print(filtrar_veteranos(df_jugadores))
print()


# Ejercicio 3: Combinación y Mapeo Condicional (Pandas)
# Recibes df_personajes ('id_pj', 'nombre', 'clase_id') y df_clases ('clase_id', 'nombre_clase', 'tier').
# 1. Haz un merge interno (inner join) usando 'clase_id'.
# 2. Elimina la columna 'clase_id' del DataFrame resultante.
# 3. Crea una nueva columna 'viabilidad' usando np.where(): 
#    Si el 'tier' es 'S' o 'A', la viabilidad debe ser 'Alta'. Si es cualquier otro, debe ser 'Normal'.
# Devuelve el DataFrame resultante.
def evaluar_meta(df_pjs, df_clases):
    return (pd.merge(df_pjs, df_clases, on='clase_id', how='inner')
            .drop(columns=['clase_id'])
            .assign(viabilidad=lambda x: np.where(x['tier'].isin(['S', 'A']), 'Alta', 'Normal')))

print("--- Ejercicio 3 ---")
df_personajes = pd.DataFrame({
    'id_pj': [1, 2, 3, 4],
    'nombre': ['Arthur', 'Merlin', 'Lancelot', 'Gawain'],
    'clase_id': [10, 20, 10, 30]
})
df_clases = pd.DataFrame({
    'clase_id': [10, 20, 30],
    'nombre_clase': ['Saber', 'Caster', 'Berserker'],
    'tier': ['A', 'S', 'C']
})
print(evaluar_meta(df_personajes, df_clases))
print()


# Ejercicio 4: Agrupación y Múltiples Agregaciones (Pandas)
# Tienes un DataFrame de estadísticas de escuderías o equipos con 'equipo', 'puntos', 'victorias' (booleano o 1/0).
# Devuelve un DataFrame agrupado por 'equipo' que contenga exactamente estas dos columnas:
# - 'puntos_totales': La suma total de los puntos.
# - 'win_rate': La media de la columna victorias (esto dará el porcentaje de victorias).
# El DataFrame final debe estar ordenado de mayor a menor 'win_rate'.
def ranking_equipos(df_partidas):
    return (df_partidas.groupby('equipo')
            .agg(puntos_totales=('puntos', 'sum'), win_rate=('victorias', 'mean'))
            .sort_values(by='win_rate', ascending=False))

print("--- Ejercicio 4 ---")
df_stats = pd.DataFrame({
    'equipo': ['Spica', 'Rigil', 'Spica', 'Canopus', 'Rigil', 'Spica'],
    'puntos': [100, 85, 120, 60, 90, 110],
    'victorias': [1, 0, 1, 0, 1, 1]
})
print(ranking_equipos(df_stats))
print()