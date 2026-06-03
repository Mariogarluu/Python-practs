import pandas as pd
import numpy as np

# Ejercicio 1: Ordenación Multicriterio y Excepciones (Python Puro)
# Recibes una lista de diccionarios de empleados con 'nombre', 'departamento' y 'rendimiento'.
# 1. Filtra los empleados descartando aquellos que no tengan la clave 'rendimiento' 
#    o cuyo rendimiento no sea un número válido (maneja las excepciones).
# 2. Ordena la lista resultante con un doble criterio: 
#    Primero alfabéticamente por 'departamento', y en caso de empate, por 'rendimiento' de MAYOR a MENOR.
# 3. Devuelve una lista de tuplas con el formato: (nombre, departamento, rendimiento).
# REGLA: Haz la ordenación utilizando la función sorted() y una función lambda.
def ranking_empleados(plantilla):
    validos = [emp for emp in plantilla if 'rendimiento' in emp and isinstance(emp['rendimiento'], (int, float))]
    return [(emp['nombre'], emp['departamento'], emp['rendimiento']) 
            for emp in sorted(validos, key=lambda x: (x['departamento'], -x['rendimiento']))]

print("--- Ejercicio 1 ---")
empleados = [
    {'nombre': 'Ana', 'departamento': 'IT', 'rendimiento': 95},
    {'nombre': 'Luis', 'departamento': 'Ventas', 'rendimiento': 88},
    {'nombre': 'Marta', 'departamento': 'IT', 'rendimiento': 99},
    {'nombre': 'Pedro', 'departamento': 'Ventas', 'rendimiento': "N/A"}, # Error
    {'nombre': 'Carlos', 'departamento': 'HR'}, # Falta clave
    {'nombre': 'Sofia', 'departamento': 'Ventas', 'rendimiento': 92}
]
print(ranking_empleados(empleados))
print()


# Ejercicio 2: Series Temporales y Atributos de Fecha (Pandas)
# Tienes un DataFrame de ventas con 'id_ticket', 'fecha' y 'total'.
# 1. Convierte 'fecha' a datetime (forzando errores a NaT).
# 2. Elimina las filas con fechas inválidas (NaT).
# 3. Usa el accesor '.dt' para crear una nueva columna llamada 'mes' que contenga 
#    el número del mes (1 al 12) extraído de la columna 'fecha'.
# 4. Agrupa por 'mes' y calcula la suma del 'total'.
# Devuelve la Serie o DataFrame resultante ordenado por mes.
def reporte_mensual(df):
    return (df.assign(fecha=lambda x: pd.to_datetime(x['fecha'], errors='coerce'))
            .dropna(subset=['fecha'])
            .assign(mes=lambda x: x['fecha'].dt.month)
            .groupby('mes')['total'].sum())

print("--- Ejercicio 2 ---")
df_ventas = pd.DataFrame({
    'id_ticket': [1, 2, 3, 4, 5],
    'fecha': ['2026-01-15', '2026-02-10', 'Fecha Rota', '2026-01-22', '2026-03-05'],
    'total': [150.5, 200.0, 50.0, 320.0, 110.0]
})
print(reporte_mensual(df_ventas))
print()


# Ejercicio 3: Métricas Relativas / Porcentajes (Pandas)
# Recibes un DataFrame de ingresos por 'canal' de marketing y el 'coste_campaña'.
# 1. Agrupa por 'canal' calculando el total de 'ingresos'.
# 2. El método .agg() te devolverá un DataFrame. Usando .assign(), crea una columna 
#    llamada 'porcentaje_total' que calcule qué porcentaje representa cada canal 
#    sobre la suma TOTAL de todos los ingresos de todos los canales. 
#    (Fórmula: ingresos_del_canal / suma_de_todos_los_ingresos * 100).
# 3. Ordena descendentemente por el porcentaje.
def analizar_roi_canales(df):
    return (df.groupby('canal')[['ingresos']].sum()
            .assign(porcentaje_total=lambda x: (x['ingresos'] / x['ingresos'].sum()) * 100)
            .sort_values(by='porcentaje_total', ascending=False))

print("--- Ejercicio 3 ---")
df_marketing = pd.DataFrame({
    'canal': ['SEO', 'Ads', 'Social', 'SEO', 'Ads'],
    'ingresos': [5000, 8000, 2000, 3000, 2000]
})
print(analizar_roi_canales(df_marketing))
print()


# Ejercicio 4: El "Jefe Final" del Method Chaining (Pandas)
# Recibes df_pedidos ('id_pedido', 'id_cliente', 'cantidad', 'precio_unitario').
# Construye un UNICO encadenamiento de métodos para:
# 1. Crear la columna 'subtotal' (cantidad * precio_unitario).
# 2. Agrupar por 'id_cliente'.
# 3. Calcular el 'gasto_total' (suma del subtotal) y el 'total_articulos' (suma de cantidad).
# 4. Filtrar el DataFrame resultante para quedarte SOLO con los clientes cuyo 'gasto_total' sea estrictamente mayor a 500.
# 5. Ordenar por 'gasto_total' de forma descendente.
# REGLA: No puedes romper la cadena ni declarar variables intermedias.
def clientes_vip(df):
    return (df.assign(subtotal=lambda x: x['cantidad'] * x['precio_unitario'])
            .groupby('id_cliente')[['subtotal', 'cantidad']]
            .sum()
            .rename(columns={'subtotal': 'gasto_total', 'cantidad': 'total_articulos'})
            .loc[lambda x: x['gasto_total'] > 500]
            .sort_values(by='gasto_total', ascending=False))

print("--- Ejercicio 4 ---")
df_pedidos = pd.DataFrame({
    'id_pedido': [101, 102, 103, 104, 105],
    'id_cliente': ['C1', 'C2', 'C1', 'C3', 'C2'],
    'cantidad': [2, 1, 5, 10, 3],
    'precio_unitario': [150.0, 600.0, 50.0, 20.0, 100.0]
})
print(clientes_vip(df_pedidos))
print()