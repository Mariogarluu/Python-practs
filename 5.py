import pandas as pd
import numpy as np

# Ejercicio 1: Comprensión de diccionarios y filtrado (Python Puro)
# Recibes una lista de diccionarios de componentes de PC con 'modelo', 'tipo', 'precio' y 'cl'.
# Debes devolver un diccionario donde la clave sea el 'modelo' y el valor sea el 'precio'.
# CONDICIONES: 
# 1. Solo incluye componentes de tipo "RAM" o "GPU".
# 2. Si es "RAM", solo inclúyela si su latencia 'cl' es menor o igual a 30.
# 3. Hazlo en UNA SOLA LÍNEA de código utilizando un "dictionary comprehension".
def filtrar_hardware_entusiasta(inventario):
    return {pieza['modelo']: pieza['precio'] 
            for pieza in inventario 
            if pieza['tipo'] in ['RAM', 'GPU'] and (pieza['tipo'] != 'RAM' or pieza.get('cl', float('inf')) <= 30)}

print("--- Ejercicio 1 ---")
piezas = [
    {'modelo': 'DDR5 Trident Z5', 'tipo': 'RAM', 'precio': 140, 'cl': 30},
    {'modelo': 'DDR5 Corsair', 'tipo': 'RAM', 'precio': 110, 'cl': 36},
    {'modelo': 'RTX 4080 Super', 'tipo': 'GPU', 'precio': 1050, 'cl': None},
    {'modelo': 'Ryzen 7 7800X3D', 'tipo': 'CPU', 'precio': 380, 'cl': None}
]
print(filtrar_hardware_entusiasta(piezas))
print()


# Ejercicio 2: Limpieza y Method Chaining extremo (Pandas)
# Recibes un DataFrame de personajes con 'nombre', 'stamina', 'velocidad' y 'rango'.
# Aplica un único flujo de Method Chaining para:
# 1. Eliminar filas donde el 'nombre' sea nulo.
# 2. Rellenar los nulos de 'stamina' con la mediana de 'stamina'.
# 3. Usar .assign() para crear una columna 'stats_totales' (stamina + velocidad).
# 4. Usar .loc[] y una función lambda para filtrar solo aquellos con 'stats_totales' > 1500.
# Devuelve el DataFrame resultante.
def procesar_stats_training(df):
    return (df.dropna(subset=['nombre'])
            .assign(stamina=lambda x: x['stamina'].fillna(x['stamina'].median()))
            .assign(stats_totales=lambda x: x['stamina'] + x['velocidad'])
            .loc[lambda x: x['stats_totales'] > 1500])

print("--- Ejercicio 2 ---")
df_uma = pd.DataFrame({
    'nombre': ['Special Week', 'Silence Suzuka', np.nan, 'Gold Ship', 'Tokai Teio'],
    'stamina': [800.0, np.nan, 500.0, 950.0, 700.0],
    'velocidad': [850.0, 950.0, 600.0, 700.0, 900.0],
    'rango': ['A', 'S', 'B', 'A', 'S']
})
print(procesar_stats_training(df_uma))
print()


# Ejercicio 3: Cruce avanzado y np.select (Pandas)
# Recibes df_ventas ('id_vendedor', 'mes', 'facturado') y df_objetivos ('id_vendedor', 'meta').
# 1. Combina ambos DataFrames (inner join).
# 2. Usa .assign() para crear una columna 'rendimiento'. Utiliza np.where():
#    - Si 'facturado' es mayor o igual a 'meta', el valor debe ser 'Objetivo Cumplido'.
#    - En caso contrario, 'Bajo Rendimiento'.
# 3. Devuelve el DataFrame descartando la columna 'meta'.
def evaluar_rendimiento_empleados(df_v, df_o):
    return (pd.merge(df_v, df_o, on='id_vendedor', how='inner')
            .assign(rendimiento=lambda x: np.where(
                x['facturado'] >= x['meta'],
                'Objetivo Cumplido',
                'Bajo Rendimiento'
            ))
            .drop(columns=['meta']))

print("--- Ejercicio 3 ---")
df_ventas = pd.DataFrame({
    'id_vendedor': [1, 2, 1, 3],
    'mes': ['Enero', 'Enero', 'Febrero', 'Enero'],
    'facturado': [5000, 2000, 6500, 8000]
})
df_objetivos = pd.DataFrame({
    'id_vendedor': [1, 2, 3],
    'meta': [4000, 3000, 8000]
})
print(evaluar_rendimiento_empleados(df_ventas, df_objetivos))
print()


# Ejercicio 4: Agrupación múltiple y renombrado vectorial (Pandas)
# Recibes un DataFrame con registros de transacciones: 'departamento', 'tipo_gasto', 'importe'.
# 1. Agrupa por 'departamento' y 'tipo_gasto' (las dos columnas).
# 2. Calcula el gasto total ('sum') y el número de transacciones ('count') del 'importe'.
# 3. Renombra las métricas agregadas directamente dentro de la función .agg() 
#    (ej: total_gastado=('importe', 'sum'), num_operaciones=('importe', 'count')).
# 4. Ordena por 'total_gastado' de forma descendente.
def reporte_financiero_departamentos(df):
    return (df.groupby(['departamento', 'tipo_gasto'])
            .agg(total_gastado=('importe', 'sum'), num_operaciones=('importe', 'count'))
            .sort_values(by='total_gastado', ascending=False))

print("--- Ejercicio 4 ---")
df_transacciones = pd.DataFrame({
    'departamento': ['IT', 'HR', 'IT', 'Ventas', 'HR', 'IT'],
    'tipo_gasto': ['Hardware', 'Eventos', 'Software', 'Viajes', 'Nóminas', 'Hardware'],
    'importe': [2500, 500, 120, 1500, 4000, 800]
})
print(reporte_financiero_departamentos(df_transacciones))
print()