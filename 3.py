import pandas as pd
import numpy as np

# SIMULACRO INTEGRAL: PIPELINE DE GESTIÓN DE INVENTARIO
# Se te proporcionan dos DataFrames simulando una extracción de base de datos relacional.

df_inventario = pd.DataFrame({
    'id_comp': [1, 2, 3, 4, 5, 6],
    'nombre_x': ['RTX 4090', 'Ryzen 7 7800X3D', 'DDR5 32GB 6000MHz', 'SSD 2TB Gen4', 'RTX 4070 Ti', 'Fuente 1000W'],
    'precio': [1800.50, np.nan, 120.0, 150.0, np.nan, 200.0],
    'stock': [5.0, 15.0, 50.0, 0.0, 12.0, np.nan],
    'id_proveedor': [101, 102, 101, 103, 101, 102]
})

df_proveedores = pd.DataFrame({
    'id_proveedor': [101, 102, 103],
    'nombre_y': ['TechGlobal', 'SiliconVal', 'DataStore']
})


# Parte 1: Combinación, Renombrado y Limpieza (Temas 5 y 6)
# 1. Haz un merge 'left' del inventario con los proveedores usando 'id_proveedor'.
# 2. Renombra 'nombre_x' a 'componente' y 'nombre_y' a 'proveedor'.
# 3. Rellena los NaN en 'precio' con la mediana de la columna.
# 4. Rellena los NaN en 'stock' con 0.
# 5. Convierte la columna 'stock' a tipo entero (int).
# Devuelve el DataFrame resultante.
def limpiar_y_combinar(df_inv, df_prov):
    return (pd.merge(df_inv, df_prov, on='id_proveedor', how='left')
            .rename(columns={'nombre_x': 'componente', 'nombre_y': 'proveedor'})
            .assign(
                precio=lambda df: df['precio'].fillna(df['precio'].median()),
                stock=lambda df: df['stock'].fillna(0).astype(int)
            ))


# Parte 2: Indexación y Mapeo (Temas 2 y 3)
# 1. Crea una columna 'valor_total' que sea el resultado de multiplicar 'precio' por 'stock'.
# 2. Usando la sintaxis de .loc y operadores a nivel de bits (&, |):
#    Filtra los registros donde el 'componente' contenga el texto "RTX" o "DDR5" (usa .str.contains()) 
#    Y cuyo 'stock' sea estrictamente mayor a 0.
# Devuelve el DataFrame filtrado.
def filtrar_alto_rendimiento(df_limpio):
    df_eval = df_limpio.assign(valor_total=df_limpio['precio'] * df_limpio['stock'])
    
    filtro = (
        df_eval['componente'].str.contains('RTX|DDR5', case=False, na=False) & 
        (df_eval['stock'] > 0)
    )
    return df_eval.loc[filtro]


# Parte 3: Agrupación y Ordenamiento (Temas 1 y 4)
# 1. Agrupa el DataFrame limpio por la columna 'proveedor'.
# 2. Calcula métricas múltiples en una sola pasada (.agg): 
#    - El precio medio ('mean')
#    - El stock total ('sum')
# 3. Ordena el DataFrame resultante por el stock total de forma descendente.
# (En un caso real exportaríamos con .to_csv(), aquí solo devuelve el DF).
def reporte_proveedores(df_limpio):
    return (df_limpio.groupby('proveedor')
            .agg(precio_medio=('precio', 'mean'), stock_total=('stock', 'sum'))
            .sort_values(by='stock_total', ascending=False))


print("--- Parte 1: Limpieza y Combinación ---")
df_procesado = limpiar_y_combinar(df_inventario, df_proveedores)
print(df_procesado)
print("\nTipos de datos:\n", df_procesado.dtypes)
print("\n")

print("--- Parte 2: Filtrado Avanzado ---")
print(filtrar_alto_rendimiento(df_procesado))
print("\n")

print("--- Parte 3: Agrupación y Reporte ---")
print(reporte_proveedores(df_procesado))