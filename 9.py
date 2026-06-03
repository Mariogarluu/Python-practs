import pandas as pd
import numpy as np

# Ejercicio 1: Cálculo de DPS con múltiples excepciones (Python Puro)
# Recibes una lista de diccionarios de armas con 'nombre', 'daño' y 'tiempo_ataque'.
# Devuelve un diccionario {nombre_arma: dps_redondeado_a_2_decimales}.
# DPS = daño / tiempo_ataque.
# Controla explícitamente y de forma separada:
# 1. KeyError (si falta alguna clave en el diccionario).
# 2. ZeroDivisionError (si 'tiempo_ataque' es 0).
# 3. TypeError o ValueError (si los valores no son numéricos).
# Si un arma dispara cualquiera de estas excepciones, ignórala y continúa con la siguiente.
def calcular_dps_armas(inventario):
    resultado = {}
    for arma in inventario:
        try:
            dps = arma['daño'] / arma['tiempo_ataque']
            resultado[arma['nombre']] = round(dps, 2)
        except (KeyError, ZeroDivisionError, TypeError, ValueError):
            continue
    return resultado

print("--- Ejercicio 1 ---")
armas_rpg = [
    {'nombre': 'Espada Larga', 'daño': 150, 'tiempo_ataque': 1.5},
    {'nombre': 'Daga Rota', 'daño': 40, 'tiempo_ataque': 0},       # ZeroDivisionError
    {'nombre': 'Martillo Pesado', 'daño': 300},                    # KeyError
    {'nombre': 'Arco Élfico', 'daño': 'Cien', 'tiempo_ataque': 1}, # ValueError/TypeError
    {'nombre': 'Alabarda', 'daño': 210, 'tiempo_ataque': 2.0}
]
print(calcular_dps_armas(armas_rpg))
print()


# Ejercicio 2: Parsing de logs de hardware (Python Puro)
# Recibes una lista de strings con el formato exacto: "GPU_ID: [ID] | Temp: [Valor]C"
# Devuelve una lista de tuplas (ID_entero, Temp_float).
# Usa try-except para capturar:
# 1. ValueError (al intentar convertir el ID a int o la Temperatura a float).
# 2. IndexError (si el string está corrupto y no tiene las partes necesarias al hacer split).
# Los registros que fallen deben ser descartados.
def parsear_sensores_gpu(lecturas):
    resultado = []
    for lectura in lecturas:
        try:
            partes = lectura.split(' | ')
            id_gpu = int(partes[0].split(': ')[1])
            temp = float(partes[1].split(': ')[1][:-1])
            resultado.append((id_gpu, temp))
        except (ValueError, IndexError):
            continue
    return resultado

print("--- Ejercicio 2 ---")
logs_temperatura = [
    "GPU_ID: 101 | Temp: 75.5C",
    "GPU_ID: 102 | Temp: 80.0C",
    "GPU_ID: XYZ | Temp: 90.0C",        # ValueError al convertir ID
    "Registro corrupto de red",         # IndexError al hacer split
    "GPU_ID: 104 | Temp: ErrorC"        # ValueError al convertir Temp
]
print(parsear_sensores_gpu(logs_temperatura))
print()


# Ejercicio 3: Interfaz segura para Pandas (Pandas + Excepciones)
# Recibes un DataFrame, el nombre de una columna de agrupación (col_grupo) 
# y el nombre de una columna a sumar (col_calc).
# Intenta agrupar por col_grupo y devolver la suma de col_calc usando Method Chaining.
# Si alguna de las columnas no existe en el DataFrame, la operación lanzará un KeyError.
# Captura ese KeyError y devuelve el string: "Error: Columnas no encontradas".
def agrupacion_segura(df, col_grupo, col_calc):
    try:
        return df.groupby(col_grupo)[col_calc].sum()
    except KeyError:
        return "Error: Columnas no encontradas"

print("--- Ejercicio 3 ---")
df_ventas = pd.DataFrame({
    'region': ['Norte', 'Sur', 'Norte', 'Este'],
    'ingresos': [1000, 2000, 1500, 3000]
})
print(agrupacion_segura(df_ventas, 'region', 'ingresos'))
print(agrupacion_segura(df_ventas, 'zona', 'ingresos')) # Dispara KeyError
print()


# Ejercicio 4: Limpieza compleja con apply y try-except (Pandas)
# Tienes un DataFrame con una columna 'precio_bruto' que contiene mezclas de 
# números limpios, strings con símbolos ("$45.50", "30€"), o textos corruptos ("Gratis", "N/A").
# 1. Crea una función interna (def limpiar_valor(x):) que use try-except. 
#    Esta función debe quitar los símbolos '$' y '€', y luego intentar convertir a float. 
#    Si ocurre un ValueError, debe devolver np.nan.
# 2. Usa .assign() y .apply() para aplicar esta función y crear la columna 'precio_neto'.
# 3. Elimina las filas donde 'precio_neto' sea NaN.
def procesar_precios_corruptos(df):
    def limpiar_valor(x):
        try:
            return float(str(x).replace('$', '').replace('€', ''))
        except (ValueError, AttributeError):
            return np.nan
    return (df.assign(precio_neto=lambda x: x['precio_bruto'].apply(limpiar_valor))    
            .dropna(subset=['precio_neto']))

print("--- Ejercicio 4 ---")
df_presupuestos = pd.DataFrame({
    'item': ['Monitor', 'Teclado', 'Ratón', 'Cable', 'Soporte'],
    'precio_bruto': ['$300.00', '120.50€', 'Gratis', '15', 'N/A']
})
print(procesar_precios_corruptos(df_presupuestos))
print()