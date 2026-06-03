import pandas as pd
import numpy as np

# Ejercicio 1: Lógica de Presupuestos y Diccionarios (Python Puro)
# Recibes una lista de diccionarios con el hardware planificado para un ensamble: 'componente', 'tipo', 'precio'.
# 1. Calcula el coste total del presupuesto.
# 2. Aplica un 15% de descuento EXCLUSIVAMENTE a los componentes cuyo 'tipo' sea 'GPU' o 'RAM'.
# 3. Ignora los componentes que no tengan precio o cuyo precio sea un string corrupto.
# 4. Devuelve una tupla: (coste_total_original, coste_final_con_descuento), ambos redondeados a 2 decimales.
def calcular_presupuesto_ensamble(piezas):
    total = 0
    descuento = 0
    for pieza in piezas:
        if 'precio' in pieza:
            try:
                precio = float(pieza['precio'])
                total += precio
                if pieza['tipo'] in ['GPU', 'RAM']:
                    descuento += precio * 0.15
            except (ValueError, TypeError):
                continue
    return (round(total, 2), round(total - descuento, 2))

print("--- Ejercicio 1 ---")
hardware_2026 = [
    {'componente': 'RTX 5090', 'tipo': 'GPU', 'precio': 1999.99},
    {'componente': 'Ryzen 9', 'tipo': 'CPU', 'precio': 549.50},
    {'componente': 'DDR5 64GB', 'tipo': 'RAM', 'precio': 220.00},
    {'componente': 'Placa Base X870', 'tipo': 'Motherboard', 'precio': "Agotado"},
    {'componente': 'Fuente 1200W', 'tipo': 'PSU'}
]
print(calcular_presupuesto_ensamble(hardware_2026))
print()


# Ejercicio 2: Fechas, Mapeo y Limpieza en Redes Sociales (Pandas)
# Tienes un DataFrame con datos de usuarios de una app de tracking social: 'user', 'fecha_registro', 'dias_inactivo'.
# 1. Convierte 'fecha_registro' a datetime. Si hay errores, conviértelos a NaT (Not a Time).
# 2. Elimina las filas donde 'fecha_registro' sea NaT.
# 3. Rellena los nulos de 'dias_inactivo' con 0.
# 4. Usando np.where, crea una columna 'estado_cuenta': si 'dias_inactivo' > 30 es 'Inactiva', sino 'Activa'.
# Devuelve el DataFrame usando Method Chaining.
def auditar_usuarios_app(df):
    return (df.assign(fecha_registro = lambda x: pd.to_datetime(x['fecha_registro'], errors='coerce'))
            .dropna(subset=['fecha_registro'])
            .assign(dias_inactivo = lambda x: x['dias_inactivo'].fillna(0))
            .assign(estado_cuenta = lambda x: np.where(x['dias_inactivo'] > 30, 'Inactiva', 'Activa')))

print("--- Ejercicio 2 ---")
df_trackverse = pd.DataFrame({
    'user': ['UserA', 'UserB', 'UserC', 'UserD'],
    'fecha_registro': ['2026-01-15', 'Fecha Invalida', '2026-02-20', '2026-02-28'],
    'dias_inactivo': [12, np.nan, 45, 2]
})
print(auditar_usuarios_app(df_trackverse))
print()


# Ejercicio 3: Agrupación y Probabilidades Gacha (Pandas)
# Tienes un DataFrame del histórico de tiradas en un banner: 'carta_apoyo', 'tier', 'tipo_banner', 'aciertos', 'total_tiradas'.
# 1. Agrupa por 'tipo_banner' y 'tier'.
# 2. Calcula el total de 'aciertos' y el total de 'tiradas' sumando las columnas respectivas.
# 3. Crea una columna 'probabilidad_obtencion' que sea (aciertos / total_tiradas) * 100.
# 4. Devuelve el DataFrame ordenado por 'probabilidad_obtencion' de forma descendente.
def analizar_probabilidades_banner(df):
    return (df.groupby(['tipo_banner', 'tier'])
            .agg(aciertos=('aciertos', 'sum'), total_tiradas=('total_tiradas', 'sum'))
            .assign(probabilidad_obtencion = lambda x: (x['aciertos'] / x['total_tiradas']) * 100)
            .sort_values(by='probabilidad_obtencion', ascending=False))

print("--- Ejercicio 3 ---")
df_tiradas = pd.DataFrame({
    'carta_apoyo': ['Kitasan', 'Tazuna', 'Super Creek', 'Kitasan', 'Fine Motion'],
    'tier': ['SSR', 'SR', 'SSR', 'SSR', 'SSR'],
    'tipo_banner': ['Foco', 'Estandar', 'Foco', 'Estandar', 'Foco'],
    'aciertos': [3, 15, 1, 0, 2],
    'total_tiradas': [200, 100, 200, 50, 150]
})
print(analizar_probabilidades_banner(df_tiradas))
print()


# Ejercicio 4: Cruces Complejos y Agregaciones (Pandas)
# Tienes df_jugadores ('id', 'build') y df_jefes ('id_jugador', 'jefe', 'intentos', 'derrotado').
# 1. Une ambos DataFrames asegurando que solo queden los jugadores que se han enfrentado a jefes (inner merge).
# 2. Rellena los nulos de la columna 'derrotado' asumiendo que si es nulo, es False.
# 3. Agrupa por 'build' y 'jefe'.
# 4. Calcula la media de 'intentos' (renombrada a 'intentos_medios') y la suma de 'derrotado' (renombrada a 'victorias_totales').
def analizar_estadisticas_combate(df_jug, df_jef):
    return (pd.merge(df_jug, df_jef, left_on='id', right_on='id_jugador', how='inner')
            .drop(columns=['id', 'id_jugador'])
            .fillna({'derrotado': False})
            .groupby(['build', 'jefe'])
            .agg(intentos_medios=('intentos', 'mean'), victorias_totales=('derrotado', 'sum')))

print("--- Ejercicio 4 ---")
df_jugadores_rpg = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'build': ['Fuerza/Guts', 'Destreza', 'Fuerza/Guts', 'Magia']
})
df_jefes_dlc = pd.DataFrame({
    'id_jugador': [1, 1, 2, 3, 4, 1],
    'jefe': ['Messmer', 'Rellana', 'Messmer', 'Rellana', 'Messmer', 'Gaius'],
    'intentos': [15, 5, 40, 12, 8, 3],
    'derrotado': [True, True, False, np.nan, True, False]
})
print(analizar_estadisticas_combate(df_jugadores_rpg, df_jefes_dlc))
print()