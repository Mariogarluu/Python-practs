import pandas as pd
import numpy as np

# Ejercicio 1: Procesamiento de Catálogo de Audio (Python Puro)
# Recibes una lista de diccionarios con información de auriculares.
# 1. Filtra aquellos que tengan el codec 'LDAC'.
# 2. Aplica un 10% de descuento a su precio.
# 3. Devuelve un diccionario donde la clave sea el modelo (en mayúsculas) y 
#    el valor sea el precio final redondeado a dos decimales.
# 4. Gestiona posibles errores si falta la clave de precio o si el valor está corrupto.
def filtrar_auriculares(catalogo):
    resultado = {}
    for auricular in catalogo:
        if auricular.get('codec') == 'LDAC' and 'precio' in auricular:
            try:
                precio_final = float(auricular['precio']) * 0.90
                resultado[auricular['modelo'].upper()] = round(precio_final, 2)
            except (ValueError, TypeError):
                continue
    return resultado  


# Ejercicio 2: Análisis de Resina 3D (Pandas)
# Recibes un DataFrame con el historial de impresiones.
# 1. Agrupa los datos por el tipo de 'resina'.
# 2. Calcula el total de mililitros consumidos (suma de 'ml_usados') y 
#    la tasa de éxito de impresión (media de 'exito').
# 3. Renombra las métricas agregadas directamente a 'consumo_total' y 'tasa_exito'.
# 4. Ordena por 'tasa_exito' de forma descendente.
def analizar_impresiones(df_impresiones):
    return (df_impresiones.groupby('resina')
            .agg(consumo_total=('ml_usados', 'sum'), tasa_exito=('exito', 'mean'))
            .sort_values(by='tasa_exito', ascending=False))


# Ejercicio 3: Cruce de Datos de Usuarios (Pandas)
# Simularemos la base de datos de TrackVerse. Recibes df_usuarios y df_sesiones.
# 1. Realiza un inner merge entre ambos DataFrames usando 'id_usuario'.
# 2. Elimina la columna 'id_usuario' tras la unión.
# 3. Rellena los valores nulos de la columna 'horas_uso' con 0.0.
# 4. Filtra usando .loc[] para quedarte solo con registros donde 'horas_uso' 
#    sea estrictamente mayor a 5 y 'plataforma' sea 'Web'.
def evaluar_trackverse(df_usuarios, df_sesiones):
    return (pd.merge(df_usuarios, df_sesiones, on='id_usuario', how='inner')
            .drop(columns=['id_usuario'])
            .fillna({'horas_uso': 0.0})
            .loc[lambda x: (x['horas_uso'] > 5) & (x['plataforma'] == 'Web')])


print("--- Ejercicio 1 ---")
datos_audio = [
    {'modelo': 'Soundcore Space One', 'codec': 'LDAC', 'precio': 99.99},
    {'modelo': 'QCY H3 Pro', 'codec': 'LDAC', 'precio': 55.50},
    {'modelo': 'SteelSeries Arctis', 'codec': 'SBC', 'precio': 150.00},
    {'modelo': 'Sony WH-1000XM5', 'codec': 'LDAC', 'precio': "Error_Precio"},
    {'modelo': 'AirPods Max', 'codec': 'AAC'} 
]
print(filtrar_auriculares(datos_audio))
print()


print("--- Ejercicio 2 ---")
df_impresiones_3d = pd.DataFrame({
    'resina': ['ABS-Like', 'Standard', 'ABS-Like', 'Water-Washable', 'Standard'],
    'ml_usados': [120, 50, 200, 80, 45],
    'exito': [True, False, True, True, True]
})
print(analizar_impresiones(df_impresiones_3d))
print()


print("--- Ejercicio 3 ---")
df_usuarios_app = pd.DataFrame({
    'id_usuario': [1, 2, 3, 4],
    'nombre': ['Mario', 'Ana', 'Luis', 'Sofia'],
    'plan': ['Pro', 'Free', 'Pro', 'Free']
})
df_sesiones_app = pd.DataFrame({
    'id_usuario': [1, 1, 2, 3, 4],
    'plataforma': ['Web', 'Mobile', 'Web', 'Web', 'Mobile'],
    'horas_uso': [12.5, 3.0, np.nan, 8.0, 4.5]
})
print(evaluar_trackverse(df_usuarios_app, df_sesiones_app))
print()