import pandas as pd
import numpy as np

# Ejercicio 1: Extracción de Logs (Python Puro)
# Recibes una lista de strings con el formato "ID-Accion-Estado". 
# Devuelve un diccionario donde la clave sea el ID (convertido a entero) y 
# el valor sea el conteo de cuántas veces ese ID ha tenido el estado "ERROR".
# Ignora los registros que lancen IndexError (falta de guiones) o ValueError (ID no convertible).
def auditar_logs_errores(logs):
    conteo = {}
    for log in logs:
        try:
            partes = log.split('-')
            id_valido = int(partes[0])
            if partes[2] == "ERROR":
                conteo[id_valido] = conteo.get(id_valido, 0) + 1
        except (IndexError, ValueError):
            continue
    return conteo


# Ejercicio 2: Consumo Eléctrico Anidado (Python Puro)
# Recibes una lista de diccionarios que representan componentes de PC. 
# Algunos tienen la clave 'specs' que es otro diccionario con la clave 'w' (vatios).
# Devuelve la suma total de los vatios. 
# Usa try-except para capturar KeyError (si falta 'specs' o 'w') y 
# TypeError/ValueError (si el valor de 'w' está corrupto), saltando esos componentes.
def calcular_consumo_total(componentes):
    total = 0
    for comp in componentes:
        try:
            total += comp['specs']['w']
        except (KeyError, TypeError, ValueError):
            continue
    return total

# Ejercicio 3: Fechas y Tiempos de Sesión (Pandas)
# Recibes un DataFrame con 'id_user', 'login' y 'logout'.
# 1. Convierte ambas columnas a datetime (forzando errores a NaT).
# 2. Elimina las filas donde alguna de las dos fechas sea NaT.
# 3. Crea la columna 'minutos_sesion' restando 'login' a 'logout' y 
#    extrayendo los minutos usando el accesor .dt.total_seconds() / 60.
# 4. Devuelve el DataFrame filtrando solo las sesiones mayores a 30 minutos.
def analizar_sesiones(df):
    return (df.assign(
                login=lambda x: pd.to_datetime(x['login'], errors='coerce'),
                logout=lambda x: pd.to_datetime(x['logout'], errors='coerce')
            )
            .dropna(subset=['login', 'logout'])
            .assign(minutos_sesion=lambda x: (x['logout'] - x['login']).dt.total_seconds() / 60)
            .loc[lambda x: x['minutos_sesion'] > 30])


# Ejercicio 4: Limpieza de Texto Numérico (Pandas)
# Recibes un DataFrame con componentes y su 'capacidad_ram' en strings sucios ("16 GB", "32GB", "Error", NaN).
# Crea una columna 'ram_limpia' quitando "GB" y " GB", intentando convertir a float. 
# Usa .assign(), funciones de string de Pandas y pd.to_numeric(errors='coerce'). 
# Rellena los nulos finales con 8.0.
def limpiar_capacidades(df):
    return (df.assign(ram_limpia=lambda x: pd.to_numeric(
                x['capacidad_ram'].astype(str).str.replace(r'\s*GB', '', regex=True), 
                errors='coerce'))
            .fillna({'ram_limpia': 8.0}))


# Ejercicio 5: Merge y np.where Avanzado (Pandas)
# Recibes df_personajes y df_stamina. 
# 1. Haz un inner merge por 'id'.
# 2. Crea una columna 'estado' usando np.where: 
#    Si stamina < 400 -> 'Descanso'. Si es mayor o igual -> 'Entrenamiento'.
# 3. Elimina la columna 'id' al final.
def gestionar_entrenamiento(df_pjs, df_stam):
    return (pd.merge(df_pjs, df_stam, on='id', how='inner')
            .assign(estado=lambda x: np.where(x['stamina'] < 400, 'Descanso', 'Entrenamiento'))
            .drop(columns=['id']))

# Ejercicio 6: Agrupación y Aplanamiento MultiIndex (Pandas)
# Recibes un DataFrame de enemigos derrotados con 'zona', 'tipo' y 'almas'.
# 1. Agrupa por 'zona' y 'tipo'. 
# 2. Calcula la suma y el máximo de 'almas'.
# 3. Aplana las columnas resultantes (ej: 'almas_sum', 'almas_max') 
#    sobrescribiendo df.columns de forma limpia y devuelve el DataFrame modificado.
def reporte_farmeo(df):
    agrupado = df.groupby(['zona', 'tipo'])[['almas']].agg(['sum', 'max'])
    agrupado.columns = [f"{col}_{agg}" for col, agg in agrupado.columns]
    return agrupado.reset_index()


# Ejercicio 7: Mapeo y Valores por Defecto (Pandas)
# Recibes un DataFrame de ventas con 'id_canal' y un diccionario 'mapa_canales'.
# 1. Usa .assign() y .map() para crear la columna 'canal_nombre'.
# 2. Aplica un .fillna() para que, si el id_canal no estaba en el mapa, 
#    el valor en 'canal_nombre' sea "Otro".
def mapear_canales(df, mapa):
    return df.assign(canal_nombre=lambda x: x['id_canal'].map(mapa)).fillna({'canal_nombre': 'Otro'})


# Ejercicio 8: El Mega-Pipeline de Producción (Pandas)
# Recibes df_pedidos y df_precios. En UNA SOLA cadena ininterrumpida:
# 1. Haz un inner merge por 'id_producto'.
# 2. Crea 'subtotal' multiplicando 'cantidad' por 'precio'.
# 3. Agrupa por 'cliente'.
# 4. Calcula el total gastado sumando el 'subtotal' (usa .agg() para nombrarlo).
# 5. Filtra (.loc) a los clientes con gasto mayor a 1000.
# 6. Ordena descendentemente.
def facturacion_vip(df_ped, df_prec):
    return (pd.merge(df_ped, df_prec, on='id_producto', how='inner')
            .assign(subtotal=lambda x: x['cantidad'] * x['precio'])
            .groupby('cliente')
            .agg(total_gastado=('subtotal', 'sum'))
            .reset_index()
            .loc[lambda x: x['total_gastado'] > 1000]
            .sort_values(by='total_gastado', ascending=False))


print("--- Ejercicio 1 ---")
logs_server = [
    "101-Login-OK",
    "102-Query-ERROR",
    "101-Upload-ERROR",
    "ABC-Hack-ERROR",
    "103-Timeout"
]
print(auditar_logs_errores(logs_server))
print()

print("--- Ejercicio 2 ---")
hardware_build = [
    {'pieza': 'GPU', 'specs': {'w': 350.5}},
    {'pieza': 'CPU', 'specs': {'w': 105}},
    {'pieza': 'RAM', 'specs': {'rgb': True}},
    {'pieza': 'Ventilador', 'specs': {'w': "Quince"}},
    {'pieza': 'Caja'}
]
print(calcular_consumo_total(hardware_build))
print()

print("--- Ejercicio 3 ---")
df_conexiones = pd.DataFrame({
    'id_user': [1, 2, 3],
    'login': ['2026-06-03 14:00:00', 'FechaRota', '2026-06-03 15:00:00'],
    'logout': ['2026-06-03 14:45:00', '2026-06-03 16:00:00', '2026-06-03 15:10:00']
})
print(analizar_sesiones(df_conexiones))
print()

print("--- Ejercicio 4 ---")
df_rams = pd.DataFrame({'componente': ['Mod A', 'Mod B', 'Mod C', 'Mod D'], 'capacidad_ram': ['16 GB', '32GB', 'Error', np.nan]})
print(limpiar_capacidades(df_rams))
print()

print("--- Ejercicio 5 ---")
df_chars = pd.DataFrame({'id': [1, 2], 'nombre': ['Kitasan', 'Tazuna']})
df_stam = pd.DataFrame({'id': [1, 2], 'stamina': [500, 200]})
print(gestionar_entrenamiento(df_chars, df_stam))
print()

print("--- Ejercicio 6 ---")
df_jefes = pd.DataFrame({
    'zona': ['Castillo', 'Pantano', 'Castillo'],
    'tipo': ['Jefe', 'Elite', 'Jefe'],
    'almas': [5000, 1200, 6000]
})
print(reporte_farmeo(df_jefes))
print()

print("--- Ejercicio 7 ---")
df_ventas_canal = pd.DataFrame({'venta': [100, 200, 300], 'id_canal': [1, 2, 99]})
mapa = {1: 'Web', 2: 'App'}
print(mapear_canales(df_ventas_canal, mapa))
print()

print("--- Ejercicio 8 ---")
df_ped = pd.DataFrame({'cliente': ['A', 'B', 'A'], 'id_producto': [10, 20, 10], 'cantidad': [2, 1, 5]})
df_pr = pd.DataFrame({'id_producto': [10, 20], 'precio': [200.0, 1500.0]})
print(facturacion_vip(df_ped, df_pr))
print()