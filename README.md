# 📚 Guía de Estudio Completa y Cheatsheet: Python & Pandas (DAM)

Esta guía está diseñada para que puedas **estudiar y repasar directamente desde aquí**. Cada sección explica la teoría del patrón, muestra ejemplos de código prácticos que se evalúan en clase y lista en qué ejercicios del repositorio se aplica cada técnica.

---

## 📂 Índice de Contenido de Estudio

1. [Uso de Diccionarios y Colecciones (Python Puro)](#-1-uso-de-diccionarios-y-colecciones-python-puro)
2. [Limpieza, Tratamiento de Nulos y Tipos](#-2-limpieza-tratamiento-de-nulos-y-tipos-pandas--python)
3. [Gestión de Excepciones y Tolerancia a Fallos](#-3-gestión-de-excepciones-y-tolerancia-a-fallos)
4. [Agrupaciones y Métricas (groupby & agg)](#-4-agrupaciones-y-métricas-groupby--agg)
5. [Combinación y Cruce de Tablas (merges & concat)](#-5-combinación-y-cruce-de-tablas-merges--concat)
6. [Lógica Condicional y Mapeo (np.where, np.select, .map)](#-6-lógica-condicional-y-mapeo-npwhere-npselect-map)
7. [Series Temporales y Fechas (.dt)](#-7-series-temporales-y-fechas-dt)
8. [Method Chaining Extremo (Metodología Pandas Profesional)](#-8-method-chaining-extremo-metodología-pandas-profesional)

---

## 🔑 1. Uso de Diccionarios y Colecciones (Python Puro)

### 💡 Teoría y Patrón Clave
Los diccionarios (`dict`) son estructuras clave-valor. En programación defensiva es crucial evitar el error `KeyError` (intentar acceder a una clave que no existe). Para ello, la herramienta principal es el método `.get(clave, valor_por_defecto)`.

### 💻 Ejemplos Prácticos de Código

#### A. Inicializar y Contar Frecuencias (Patrón Contador)
```python
# Contar cuántas veces se repite cada carácter en una cadena
texto = "hola chiqui"
frecuencias = {}

for char in texto:
    if char != " ":
        # Si 'char' no existe en el diccionario, .get() devuelve 0 y le suma 1
        frecuencias[char] = frecuencias.get(char, 0) + 1

print(frecuencias)  # {'h': 1, 'o': 1, 'l': 1, 'a': 1, 'c': 1, 'i': 2, 'q': 1, 'u': 1}
```

#### B. Ordenación Multicriterio (Sorted + Lambdas)
```python
# Ordenar equipamiento por Daño (de mayor a menor: signo negativo) 
# y por Peso (de menor a mayor: signo positivo en caso de empate)
armas = [
    ("Espada Larga", 50, 10), 
    ("Daga Rápida", 30, 2), 
    ("Hacha Pesada", 50, 15)
]

# x[1] es Daño, x[2] es Peso. El signo menos "-" invierte el orden (descendente)
ordenadas = sorted(armas, key=lambda x: (-x[1], x[2]))
print(ordenadas)
# [('Espada Larga', 50, 10), ('Hacha Pesada', 50, 15), ('Daga Rápida', 30, 2)]
```

### 🔗 Ejercicios para Practicar
*   **Contar frecuencias:** [1.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L50-L68) | [12.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L4-L21)
*   **Diccionarios anidados:** [1.py - Ejercicio 7](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L118-L141) | [12.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L22-L36)
*   **Ordenación con Lambdas:** [1.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L69-L82) | [11.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L4-L29)

---

## 🧹 2. Limpieza, Tratamiento de Nulos y Tipos (Pandas & Python)

### 💡 Teoría y Patrón Clave
Los datos reales suelen venir con formatos inconsistentes (nombres nulos, números con símbolos, strings corruptos). En Pandas, la limpieza consiste en rellenar valores faltantes (`.fillna()`), eliminar nulos críticos (`.dropna()`) y normalizar strings con `.str.replace()`.

### 💻 Ejemplos Prácticos de Código

#### A. Limpieza de Texto Numérico Sucio
```python
import pandas as pd

df = pd.DataFrame({'capacidad_ram': ['16 GB', '32GB', 'Error', None]})

# 1. Quitar 'GB' (ignorando espacios con una expresión regular)
# 2. Convertir a numérico (errors='coerce' convierte 'Error' o nulos en NaN)
# 3. Rellena los nulos (NaN) con un valor por defecto (8.0)
df['ram_limpia'] = (pd.to_numeric(
                        df['capacidad_ram'].astype(str).str.replace(r'\s*GB', '', regex=True),
                        errors='coerce'
                    ).fillna(8.0))

print(df)
#   capacidad_ram  ram_limpia
# 0         16 GB        16.0
# 1          32GB        32.0
# 2         Error         8.0
# 3          None         8.0
```

#### B. Eliminación y Relleno de Nulos (`dropna` vs `fillna`)
```python
# Elimina filas donde 'rango' sea nulo
df_filtrado = df.dropna(subset=['rango'])

# Rellena los nulos de una columna usando la mediana o la media de esa misma columna
df['horas_juego'] = df['horas_juego'].fillna(df['horas_juego'].median())
```

### 🔗 Ejercicios para Practicar
*   **Limpieza de Strings:** [6.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L49-L72) | [12.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L54-L65)
*   **Tratamiento de NaNs:** [3.py - Parte 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21-L35) | [4.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L37-L57)
*   **Validación pura:** [2.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L3-L34)

---

## ⚠️ 3. Gestión de Excepciones y Tolerancia a Fallos

### 💡 Teoría y Patrón Clave
Cuando se procesan archivos de logs o datos de entrada dinámicos, cualquier error de tipo (`TypeError`), índice (`IndexError`) o valor (`ValueError`) romperá el flujo. El uso defensivo de `try-except` permite capturar estos fallos individuales y registrar un mensaje de error o continuar con el siguiente registro.

### 💻 Ejemplos Prácticos de Código

#### A. Evitar Divisiones por Cero y Datos Corruptos
```python
# Dividir FPS por uso de CPU sin colapsar el programa
fps = [60, 120, 144, "caida"]
cpu = [30, 0, 50, 10]
resultados = []

for i in range(len(fps)):
    try:
        # Esto puede lanzar TypeError (si es string) o ZeroDivisionError (si cpu es 0)
        resultados.append(fps[i] / cpu[i])
    except (ZeroDivisionError, TypeError) as e:
        # En vez de colapsar, registramos el texto "ERROR"
        resultados.append("ERROR")

print(resultados)  # [2.0, 'ERROR', 2.88, 'ERROR']
```

### 🔗 Ejercicios para Practicar
*   **FPS y CPU:** [1.py - Ejercicio 6](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L95-L117)
*   **Cálculo de DPS defensivo:** [9.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L4-L34)
*   **Validación de DataFrames:** [9.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L66-L87) | [9.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L88-L107)

---

## 📊 4. Agrupaciones y Métricas (groupby & agg)

### 💡 Teoría y Patrón Clave
El agrupamiento permite segmentar un DataFrame según los valores únicos de una o más columnas. El método `.agg()` se utiliza para aplicar funciones estadísticas (`sum`, `mean`, `max`, `count`) a columnas específicas. Si aplicas múltiples agregaciones a una misma columna, Pandas genera columnas multinivel (`MultiIndex`), las cuales deben aplanarse para ser utilizables.

### 💻 Ejemplos Prácticos de Código

#### A. Agrupación y Múltiples Agregaciones Personalizadas
```python
df_partidas = pd.DataFrame({
    'equipo': ['Alfa', 'Beta', 'Alfa', 'Beta'],
    'puntos': [100, 80, 150, 90],
    'victorias': [1, 0, 1, 1]
})

# Agrupar por equipo y definir nombres de columna de salida directamente en agg
df_ranking = (df_partidas.groupby('equipo')
              .agg(
                  puntos_totales=('puntos', 'sum'),
                  tasa_victorias=('victorias', 'mean')
              ))
print(df_ranking)
#         puntos_totales  tasa_victorias
# equipo                                
# Alfa               250             1.0
# Beta               170             0.5
```

#### B. Aplanamiento de Columnas MultiIndex
```python
# Cuando se agrupa y se asignan múltiples agregaciones automáticas a una columna
agrupado = df_partidas.groupby('equipo')[['puntos']].agg(['sum', 'mean'])
print(agrupado.columns)  # MultiIndex([('puntos', 'sum'), ('puntos', 'mean')])

# Método para aplanar las columnas a una sola cadena combinada
agrupado.columns = [f"{col}_{agg}" for col, agg in agrupado.columns]
agrupado = agrupado.reset_index()

print(agrupado)
#   equipo  puntos_sum  puntos_mean
# 0   Alfa         250        125.0
# 1   Beta         170         85.0
```

### 🔗 Ejercicios para Practicar
*   **Agrupación básica:** [2.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L94-L109)
*   **Múltiples métricas con renombrado:** [4.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L86-L104) | [5.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L82-L101)
*   **Aplanar MultiIndex:** [10.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L67-L86) | [12.py - Ejercicio 6](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L77-L88)

---

## 🔗 5. Combinación y Cruce de Tablas (merges & concat)

### 💡 Teoría y Patrón Clave
*   **Merge (Equivalente a JOIN):** Combina dos DataFrames de forma horizontal basándose en una columna clave en común.
    *   `how='inner'`: Solo conserva filas cuyas claves coinciden en ambos DataFrames.
    *   `how='left'`: Conserva todas las filas del DataFrame izquierdo y añade datos del derecho si coincide la clave (rellena con NaN si no).
*   **Concat (Equivalente a UNION):** Apila DataFrames verticalmente (`axis=0`) uno debajo del otro, siempre que tengan las mismas columnas.

### 💻 Ejemplos Prácticos de Código

#### A. Cruce Horizontal (`pd.merge`)
```python
df_pjs = pd.DataFrame({'id_pj': [1, 2], 'nombre': ['Goku', 'Vegeta'], 'clase_id': [10, 20]})
df_clases = pd.DataFrame({'clase_id': [10, 20], 'tier': ['S', 'A']})

# Unir por la clave 'clase_id' y eliminar la columna de ID sobrante
df_unido = pd.merge(df_pjs, df_clases, on='clase_id', how='inner').drop(columns=['clase_id'])
print(df_unido)
#    id_pj  nombre tier
# 0      1    Goku    S
# 1      2  Vegeta    A
```

#### B. Unión Vertical (`pd.concat`)
```python
df_enero = pd.DataFrame({'mes': ['Enero'], 'ventas': [1000]})
df_febrero = pd.DataFrame({'mes': ['Febrero'], 'ventas': [1500]})

# Apilar los DataFrames
df_anual = pd.concat([df_enero, df_febrero], ignore_index=True)
print(df_anual)
#        mes  ventas
# 0    Enero    1000
# 1  Febrero    1500
```

### 🔗 Ejercicios para Practicar
*   **Merges:** [3.py - Parte 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21-L35) | [4.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59-L84) | [12.py - Ejercicio 5](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66-L76)
*   **Concatenación:** [10.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L34-L52)

---

## 🧠 6. Lógica Condicional y Mapeo (np.where, np.select, .map)

### 💡 Teoría y Patrón Clave
Evita el uso de bucles `for` en Pandas para evaluar condiciones. Utiliza las siguientes funciones vectorizadas de NumPy y Pandas:
*   `np.where(condición, valor_si_true, valor_si_false)`: Para bifurcaciones binarias simples.
*   `np.select(lista_de_condiciones, lista_de_opciones, default)`: Para múltiples condiciones lógicas consecutivas.
*   `df['col'].map(diccionario)`: Para traducir o mapear IDs/códigos en nombres de forma masiva.

### 💻 Ejemplos Prácticos de Código

#### A. Clasificación Binaria y Múltiple
```python
import numpy as np

df = pd.DataFrame({'stamina': [500, 200, 350]})

# np.where para clasificar en dos estados posibles
df['estado'] = np.where(df['stamina'] < 400, 'Descanso', 'Entrenamiento')

# np.select para múltiples opciones
condiciones = [
    df['stamina'] < 300,
    df['stamina'].between(300, 450),
    df['stamina'] > 450
]
opciones = ['Cansado', 'Normal', 'Excelente']

df['rendimiento'] = np.select(condiciones, opciones, default='Desconocido')
print(df)
#    stamina         estado rendimiento
# 0      500  Entrenamiento   Excelente
# 1      200       Descanso     Cansado
# 2      350       Descanso      Normal
```

#### B. Mapeo con Diccionarios
```python
df_ventas = pd.DataFrame({'id_canal': [1, 2, 99]})
mapa_canales = {1: 'Web', 2: 'App'}

# Mapear el ID y rellenar nulos si el canal no está en el mapa
df_ventas['canal_nombre'] = df_ventas['id_canal'].map(mapa_canales).fillna('Otro')
print(df_ventas)
#    id_canal canal_nombre
# 0         1          Web
# 1         2          App
# 2        99         Otro
```

### 🔗 Ejercicios para Practicar
*   **np.where:** [4.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59-L84) | [12.py - Ejercicio 5](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66-L76)
*   **np.select:** [5.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L52-L80)
*   **Mapeos:** [12.py - Ejercicio 7](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L89-L97)

---

## 📅 7. Series Temporales y Fechas (.dt)

### 💡 Teoría y Patrón Clave
Pandas dispone del accesor `.dt` que permite extraer información de campos tipo `datetime`. Permite obtener el mes (`.dt.month`), el año, el nombre del día, o calcular diferencias de tiempo (duración) en segundos o minutos.

### 💻 Ejemplos Prácticos de Código

#### A. Extraer Meses y Agrupar Ventas
```python
df = pd.DataFrame({
    'fecha': ['2026-01-15', '2026-02-10', 'Invalida'],
    'total': [100, 200, 50]
})

# 1. Convertir a datetime forzando fallos a NaT (Not a Time)
# 2. Quitar filas con NaT
# 3. Extraer el mes numérico (1 al 12)
# 4. Agrupar e integrar totales por mes
df_mensual = (df.assign(fecha=pd.to_datetime(df['fecha'], errors='coerce'))
              .dropna(subset=['fecha'])
              .assign(mes=lambda x: x['fecha'].dt.month)
              .groupby('mes')['total'].sum())

print(df_mensual)
# mes
# 1    100
# 2    200
# Name: total, dtype: int64
```

#### B. Calcular Duración de Sesiones (Diferencia de Timestamps)
```python
df_sesiones = pd.DataFrame({
    'login': pd.to_datetime(['2026-06-03 14:00:00']),
    'logout': pd.to_datetime(['2026-06-03 14:45:00'])
})

# Restar timestamps para conseguir un timedelta, y convertirlo a minutos absolutos
df_sesiones['minutos_sesion'] = (df_sesiones['logout'] - df_sesiones['login']).dt.total_seconds() / 60
print(df_sesiones)
#                 login              logout  minutos_sesion
# 0 2026-06-03 14:00:00 2026-06-03 14:45:00            45.0
```

### 🔗 Ejercicios para Practicar
*   **Extracción de meses:** [11.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L30-L53)
*   **Cálculo de minutos:** [12.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L37-L53)

---

## 8. Method Chaining Extremo (Metodología Pandas Profesional)

### 💡 Teoría y Patrón Clave
El encadenamiento de métodos ("Method Chaining") consiste en encadenar múltiples transformaciones de Pandas en una sola expresión utilizando paréntesis `( df.metodo1().metodo2() )`. 
*   **Regla de oro:** No puedes usar variables intermedias.
*   **Uso de lambdas:** Dentro de los métodos `.assign()` o `.loc[]`, debes usar funciones lambda (ej: `lambda x: x['col']`) para hacer referencia al estado del DataFrame modificado en el paso inmediatamente anterior del encadenamiento.

### 💻 Ejemplos Prácticos de Código

#### El Pipeline Completo e Ininterrumpido
```python
df_pedidos = pd.DataFrame({'cliente': ['A', 'B', 'A'], 'cantidad': [2, 1, 5], 'precio': [200, 1500, 200]})

# Pipeline completo: calcular subtotal, agrupar por cliente, sumar, filtrar VIPs (>1000) y ordenar
df_vip = (df_pedidos
          .assign(subtotal=lambda x: x['cantidad'] * x['precio'])
          .groupby('cliente')
          .agg(total_gastado=('subtotal', 'sum'))
          .reset_index()
          .loc[lambda x: x['total_gastado'] > 1000]
          .sort_values(by='total_gastado', ascending=False))

print(df_vip)
#   cliente  total_gastado
# 0       B           1500
# 1       A           1400
```

### 🔗 Ejercicios para Practicar
*   **Pipeline de inventario:** [3.py - Completo](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py)
*   **Chaining condicional:** [5.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L27-L50)
*   **Clientes VIP:** [11.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L76-L101)
*   **Mega-Pipeline de producción:** [12.py - Ejercicio 8](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L98-L115)
