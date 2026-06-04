# 📚 Guía de Estudio Completa y Cheatsheet: Python & Pandas (DAM)

Esta guía está diseñada para que puedas **estudiar y repasar directamente desde aquí**. Cada sección explica la teoría del patrón, muestra ejemplos de código prácticos que se evalúan en clase y lista en qué ejercicios del repositorio se aplica cada técnica.

---

## ⚡ Cheatsheet de Acceso Rápido

Esta sección es un **acordeón/resumen rápido** de sintaxis para buscar y copiar código habitual durante tus prácticas.

### 🐍 Parte 1: Python Puro (Estructuras, Excepciones y Cadenas)

| Operación / Patrón | Sintaxis / Código de Referencia | Ejercicios Relacionados |
| :--- | :--- | :--- |
| **Inicializar y contar** | `frecuencias[char] = frecuencias.get(char, 0) + 1` | [1.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L50) \| [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L4) |
| **Diccionario en una línea** | `filtrado = {p['modelo']: p['precio'] for p in inventario if ...}` | [5.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L4) |
| **Ordenar multicriterio** | `sorted(lista, key=lambda x: (-x[1], x[2]))` | [1.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L69) \| [11.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L4) |
| **Estructuras anidadas** | `try: total += comp['specs']['w'] except (KeyError, TypeError): ...` | [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L22) |
| **Parsing y split seguro** | `try: p = log.split('-'); id = int(partes[0]) except (IndexError, ValueError): ...` | [9.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L35) \| [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L4) |
| **Validación de tipos** | `if isinstance(usuario, dict) and isinstance(correo, str): ...` | [2.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L3) |

### 🐼 Parte 2: Pandas (DataFrames, Agrupaciones, Cruces y Series Temporales)

| Operación / Patrón | Sintaxis / Código de Referencia | Ejercicios Relacionados |
| :--- | :--- | :--- |
| **Method Chaining** | `(df.dropna().assign(...).loc[...])` | [3.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py) \| [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L98) |
| **Filtrado dinámico** | `.loc[lambda x: (x['nivel'] >= 100) & (x['horas'] > 50)]` | [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L37) \| [5.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L27) |
| **Tratar nulos y NaNs** | `.fillna({'col': valor})` o `.dropna(subset=['col'])` | [3.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21) \| [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L37) |
| **Agrupación y agg** | `.groupby('grupo').agg(total=('valor', 'sum'), media=('valor', 'mean'))` | [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L86) \| [5.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L82) |
| **Aplanar MultiIndex** | `df.columns = [f"{col}_{agg}" for col, agg in df.columns]` | [10.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L67) \| [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L77) |
| **Porcentaje sobre total** | `.assign(pct=lambda x: (x['ingresos'] / x['ingresos'].sum()) * 100)` | [11.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L54) |
| **Merge (Cruce JOIN)** | `pd.merge(df1, df2, on='clave', how='inner')` | [3.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21) \| [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66) |
| **np.where (binario)** | `.assign(estado=np.where(df['stamina'] < 400, 'Descanso', 'Entrenamiento'))` | [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66) \| [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59) |
| **np.select (múltiple)** | `np.select([cond1, cond2], [opc1, opc2], default='Desconocido')` | [5.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L52) |
| **Mapear con dict** | `.assign(nombre=lambda x: x['id'].map(diccionario)).fillna('Otro')` | [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L89) |
| **Filtro de conjunto** | `.loc[lambda x: x['categoria'].isin(['GPU', 'RAM'])]` | [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59) |
| **Fechas seguras (NaT)** | `pd.to_datetime(df['fecha'], errors='coerce')` | [11.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L30) \| [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L37) |
| **Duración temporal** | `df['minutos'] = (df['logout'] - df['login']).dt.total_seconds() / 60` | [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L37) |

---

## 📂 Índice de Contenido de Estudio

### 🐍 Parte 1: Python Puro (Estructuras y Excepciones)
1. [Uso de Diccionarios y Colecciones](#-1-uso-de-diccionarios-y-colecciones-python-puro)
   - [A. Inicializar y Contar Frecuencias (Patrón Contador)](#a-inicializar-y-contar-frecuencias-patrón-contador)
   - [B. Ordenación Multicriterio y Gotchas (Sorted + Lambdas)](#b-ordenación-multicriterio-y-gotchas-sorted--lambdas)
   - [C. Comprensión de Diccionarios (Dictionary Comprehensions)](#c-comprensión-de-diccionarios-dictionary-comprehensions)
   - [D. Acceso Seguro en Estructuras Anidadas](#d-acceso-seguro-en-estructuras-anidadas)
2. [Gestión de Excepciones y Tolerancia a Fallos](#-2-gestión-de-excepciones-y-tolerancia-a-fallos-python-puro)
   - [A. Evitar Divisiones por Cero y Datos Corruptos](#a-evitar-divisiones-por-cero-y-datos-corruptos)
   - [B. Parsing y Extracción Segura de Strings (Splits y Conversiones)](#b-parsing-y-extracción-segura-de-strings-splits-y-conversiones)

### 🐼 Parte 2: Pandas (DataFrames, Agrupaciones y Series Temporales)
3. [Limpieza, Tratamiento de Nulos y Tipos](#-3-limpieza-tratamiento-de-nulos-y-tipos-pandas--python)
4. [Agrupaciones y Métricas (groupby & agg)](#-4-agrupaciones-y-métricas-groupby--agg)
   - [A. Agrupación y Múltiples Agregaciones Personalizadas](#a-agrupación-y-múltiples-agregaciones-personalizadas)
   - [B. Aplanamiento de Columnas MultiIndex](#b-aplanamiento-de-columnas-multiindex)
   - [C. Cálculo de Porcentajes Relativos (Métricas sobre el Total)](#c-cálculo-de-porcentajes-relativos-métricas-sobre-el-total)
5. [Combinación y Cruce de Tablas (merges & concat)](#-5-combinación-y-cruce-de-tablas-merges--concat)
6. [Lógica Condicional y Mapeo (np.where, np.select, .map)](#-6-lógica-condicional-y-mapeo-npwhere-npselect-map)
   - [A. Clasificación Binaria y Múltiple](#a-clasificación-binaria-y-múltiple)
   - [B. Mapeo con Diccionarios](#b-mapeo-con-diccionarios)
   - [C. Comparación con Conjuntos y Listas (.isin)](#c-comparación-con-conjuntos-y-listas-isin)
7. [Series Temporales y Fechas (.dt)](#-7-series-temporales-y-fechas-dt)
   - [A. Extraer Meses y Agrupar Ventas](#a-extraer-meses-y-agrupar-ventas)
   - [B. Calcular Duración de Sesiones (Diferencia de Timestamps)](#b-calcular-duración-de-sesiones-diferencia-de-timestamps)
   - [C. Control de Fechas Inválidas (NaT) y errors='coerce'](#c-control-de-fechas-inválidas-nat-y-errorscoerce)
8. [Method Chaining Extremo (Metodología Pandas Profesional)](#-8-method-chaining-extremo-metodología-pandas-profesional)
   - [A. El Pipeline Completo e Ininterrumpido](#a-el-pipeline-completo-e-ininterrumpido)
   - [B. Filtrado Dinámico de Filas (.loc con Lambdas)](#b-filtrado-dinámico-de-filas-loc-con-lambdas)

---

## 🔑 1. Uso de Diccionarios y Colecciones (Python Puro)

### 💡 Teoría y Patrón Clave
Los diccionarios (`dict`) son estructuras clave-valor. En programación defensiva es crucial evitar el error `KeyError` (intentar acceder a una clave que no existe). Para ello, la herramienta principal es el método `.get(clave, valor_por_defecto)`. Asimismo, el uso de comprensiones de diccionario (`dictionary comprehensions`) permite filtrar y transformar listas de forma compacta en una sola línea, lo cual es muy común en exámenes. Por último, en ordenaciones complejas multivariables con strings y números, es esencial saber que **no se pueden negar cadenas de texto** con un signo menos `-`, requiriendo un manejo cuidadoso de las tuplas de ordenación.

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

#### B. Ordenación Multicriterio y Gotchas (Sorted + Lambdas)
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

# ⚠️ ¡ATENCIÓN GOTCHA DE EXAMEN!
# Si quieres ordenar por una columna de TEXTO de forma descendente y un NÚMERO ascendente,
# no puedes usar un signo menos en el texto (ej: lambda x: (-x['departamento'], x['rendimiento']) lanza TypeError).
# Solución 1: Si ambos deben ordenarse al revés, usa `reverse=True`.
# Solución 2: Realizar dos pasadas de sorted estables (gracias a que Python usa Timsort):
# Pasada 1 (criterio secundario, ej: rendimiento): sorted(lista, key=lambda x: x['rendimiento'])
# Pasada 2 (criterio primario descendente para strings): sorted(pasada1, key=lambda x: x['departamento'], reverse=True)
```

#### C. Comprensión de Diccionarios (Dictionary Comprehensions)
```python
# Convertir una lista de diccionarios en un mapa {modelo: precio} en una sola línea.
# Condición: Solo de tipo RAM o GPU. Si es RAM, además debe tener latencia 'cl' <= 30.
inventario = [
    {'modelo': 'DDR5 Trident Z5', 'tipo': 'RAM', 'precio': 140, 'cl': 30},
    {'modelo': 'DDR5 Corsair', 'tipo': 'RAM', 'precio': 110, 'cl': 36},
    {'modelo': 'RTX 4080 Super', 'tipo': 'GPU', 'precio': 1050, 'cl': None}
]

filtrado = {
    pieza['modelo']: pieza['precio'] 
    for pieza in inventario 
    if pieza['tipo'] in ['RAM', 'GPU'] and (pieza['tipo'] != 'RAM' or pieza.get('cl', float('inf')) <= 30)
}
print(filtrado)
# {'DDR5 Trident Z5': 140, 'RTX 4080 Super': 1050}
```

#### D. Acceso Seguro en Estructuras Anidadas (Manejo Defensivo)
```python
# Sumar la potencia en vatios (w) de componentes, donde algunos no tienen 'specs' o 'w'.
componentes = [
    {'pieza': 'GPU', 'specs': {'w': 350.5}},
    {'pieza': 'RAM', 'specs': {'rgb': True}}, # No tiene 'w'
    {'pieza': 'Caja'}                          # No tiene 'specs'
]

total_w = 0
for comp in componentes:
    try:
        # Esto puede lanzar KeyError si falta 'specs' o 'w', o TypeError si w no es numérico
        total_w += float(comp['specs']['w'])
    except (KeyError, TypeError, ValueError):
        continue # Ignora el componente corrupto o incompleto y continúa

print(total_w)  # 350.5
```

### 🔗 Ejercicios para Practicar
*   **Contar frecuencias:** [1.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L50-L68) | [12.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L4-L21)
*   **Diccionarios anidados y navegación segura:** [1.py - Ejercicio 7](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L118-L141) | [12.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L22-L36)
*   **Ordenación con Lambdas / Doble Criterio:** [1.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L69-L82) | [11.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L4-L29)
*   **Comprensión de Diccionarios (una sola línea):** [5.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L4-L25)

---

## ⚠️ 2. Gestión de Excepciones y Tolerancia a Fallos (Python Puro)

### 💡 Teoría y Patrón Clave
Cuando se procesan archivos de logs, entradas dinámicas o diccionarios del exterior, cualquier error de tipo (`TypeError`), índice (`IndexError`) o valor (`ValueError`) romperá el flujo del programa. El uso defensivo de `try-except` permite capturar estos fallos individuales en bucles de procesamiento, descartar la fila corrupta o registrar un mensaje y continuar con el siguiente registro sin interrumpir la ejecución global. Esto es especialmente útil para el parseo seguro de strings (uso de `.split()`) y las conversiones de tipo manuales en Python Puro.

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

#### B. Parsing y Extracción Segura de Strings (Splits y Conversiones)
```python
# Procesar logs con formato "ID-Accion-Estado". Queremos contar errores por ID.
# Debemos capturar IndexError (líneas mal formateadas) y ValueError (IDs no numéricos).
logs = [
    "101-Login-OK",
    "102-Query-ERROR",
    "101-Upload-ERROR",
    "ABC-Hack-ERROR", # ID inválido -> ValueError
    "103-Timeout"       # Falta estado -> IndexError al hacer split
]

errores_por_id = {}
for log in logs:
    try:
        partes = log.split('-')
        id_pj = int(partes[0]) # Puede lanzar ValueError
        accion = partes[1]
        estado = partes[2]     # Puede lanzar IndexError si no hay suficientes partes
        
        if estado == "ERROR":
            errores_por_id[id_pj] = errores_por_id.get(id_pj, 0) + 1
    except (IndexError, ValueError):
        continue # Descarta la línea con formato incorrecto y sigue con la siguiente

print(errores_por_id)  # {102: 1, 101: 1}
```

### 🔗 Ejercicios para Practicar
*   **FPS y CPU:** [1.py - Ejercicio 6](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L95-L117)
*   **Cálculo de DPS defensivo:** [9.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L4-L34)
*   **Parsing seguro de strings / logs:** [9.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L35-L65) | [12.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L4-L21)
*   **Validación de DataFrames:** [9.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L66-L87) | [9.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L88-L107)

---

## 🧹 3. Limpieza, Tratamiento de Nulos y Tipos (Pandas & Python)

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

## 📊 4. Agrupaciones y Métricas (groupby & agg)

### 💡 Teoría y Patrón Clave
El agrupamiento permite segmentar un DataFrame según los valores únicos de una o más columnas. El método `.agg()` se utiliza para aplicar funciones estadísticas (`sum`, `mean`, `max`, `count`) a columnas específicas. Si aplicas múltiples agregaciones a una misma columna, Pandas genera columnas multinivel (`MultiIndex`), las cuales deben aplanarse para ser utilizables. También es habitual calcular métricas relativas (como el peso porcentual de cada grupo sobre la suma global de la columna), lo cual se resuelve aplicando operaciones vectorizadas directamente sobre el total de la columna dentro de un `.assign()`.

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

#### C. Cálculo de Porcentajes Relativos (Métricas sobre el Total)
```python
# Calcular qué porcentaje de ingresos totales aporta cada canal de ventas.
# En la lambda, x['ingresos'] representa la columna agregada por canal y
# x['ingresos'].sum() es la suma de toda la columna (la suma global).
df_ventas = pd.DataFrame({
    'canal': ['SEO', 'Ads', 'Social', 'SEO', 'Ads'],
    'ingresos': [5000, 8000, 2000, 3000, 2000]
})

df_roi = (df_ventas.groupby('canal')[['ingresos']].sum()
          .assign(porcentaje_total=lambda x: (x['ingresos'] / x['ingresos'].sum()) * 100)
          .sort_values(by='porcentaje_total', ascending=False))

print(df_roi)
#          ingresos  porcentaje_total
# canal                               
# Ads         10000              50.0
# SEO          8000              40.0
# Social       2000              10.0
```

### 🔗 Ejercicios para Practicar
*   **Agrupación básica:** [2.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L94-L109)
*   **Múltiples métricas con renombrado:** [4.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L86-L104) | [5.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L82-L101)
*   **Aplanar MultiIndex:** [10.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L67-L86) | [12.py - Ejercicio 6](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L77-L88)
*   **Cálculo de Porcentajes Relativos:** [11.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L54-L73)

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
*   `df['col'].isin(lista_o_conjunto)`: Para comprobar la pertenencia a un conjunto de valores permitidos (muy usado en filtrados y dentro de `np.where`/`np.select`).

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

#### C. Comparación con Conjuntos y Listas (.isin)
```python
# Clasificar elementos según pertenezcan o no a un grupo de categorías clave (S o A)
df_heroes = pd.DataFrame({
    'nombre': ['Arthur', 'Merlin', 'Lancelot', 'Gawain'],
    'tier': ['A', 'S', 'C', 'B']
})

# .isin() devuelve una Serie booleana: True si el valor de 'tier' está en ['S', 'A']
df_heroes['viabilidad'] = np.where(df_heroes['tier'].isin(['S', 'A']), 'Alta', 'Normal')
print(df_heroes)
#      nombre tier viabilidad
# 0    Arthur    A       Alta
# 1    Merlin    S       Alta
# 2  Lancelot    C     Normal
# 3    Gawain    B     Normal
```

### 🔗 Ejercicios para Practicar
*   **np.where:** [4.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59-L84) | [12.py - Ejercicio 5](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66-L76)
*   **np.select:** [5.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L52-L80)
*   **Mapeos:** [12.py - Ejercicio 7](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L89-L97)
*   **Uso de .isin() en condiciones:** [4.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59-L84)

---

## 📅 7. Series Temporales y Fechas (.dt)

### 💡 Teoría y Patrón Clave
Pandas dispone del accesor `.dt` que permite extraer información de campos tipo `datetime`. Permite obtener el mes (`.dt.month`), el año, el nombre del día, o calcular diferencias de tiempo (duración) en segundos o minutos.

⚠️ **Gotcha Importante - Fechas Inválidas (`NaT`):** Cuando los datos de fecha vienen con formatos inconsistentes o textos rotos (ej: `"Fecha Rota"`, `"Agotado"`), el uso de `pd.to_datetime()` directo romperá el programa. Para evitarlo, debemos forzar la conversión usando el argumento **`errors='coerce'`**. Esto transformará los valores no válidos en **`NaT`** (Not a Time, el equivalente a `NaN` en fechas). Después de esta operación, es necesario limpiar el DataFrame aplicando `.dropna(subset=['nombre_columna_fecha'])` para eliminar estas filas inválidas antes de realizar agrupaciones o cálculos de duración.

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

#### C. Control de Fechas Inválidas (NaT) y errors='coerce'
```python
# Convertir y filtrar fechas inválidas en un pipeline limpio
df_usuarios = pd.DataFrame({
    'user': ['UserA', 'UserB', 'UserC'],
    'fecha_registro': ['2026-01-15', 'Fecha Invalida', '2026-02-20']
})

df_auditado = (df_usuarios
               .assign(fecha_registro=lambda x: pd.to_datetime(x['fecha_registro'], errors='coerce'))
               # Elimina la fila de UserB porque su fecha se convirtió en NaT
               .dropna(subset=['fecha_registro']))

print(df_auditado)
#    user fecha_registro
# 0  UserA     2026-01-15
# 2  UserC     2026-02-20
```

### 🔗 Ejercicios para Practicar
*   **Extracción de meses:** [11.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L30-L53)
*   **Cálculo de minutos y control de NaT:** [12.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L37-L53)
*   **Limpieza integral y estado temporal:** [7.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py#L36-L56)

---

## 🔑 8. Method Chaining Extremo (Metodología Pandas Profesional)

### 💡 Teoría y Patrón Clave
El encadenamiento de métodos ("Method Chaining") consiste en encadenar múltiples transformaciones de Pandas en una sola expresión utilizando paréntesis `( df.metodo1().metodo2() )`. 
*   **Regla de oro:** No puedes usar variables intermedias.
*   **Uso de lambdas:** Dentro de los métodos `.assign()`, `.loc[]` o `.query()`, debes usar funciones lambda (ej: `lambda x: x['col']`) para hacer referencia al estado del DataFrame modificado en el paso inmediatamente anterior del encadenamiento.
*   **Filtrado dinámico:** En lugar de hacer `df[df['precio'] > 50]`, se utiliza `.loc[lambda x: x['precio'] > 50]`. La función lambda es obligatoria porque el DataFrame original `df` no contiene todavía las columnas calculadas en los pasos previos del pipeline.

### 💻 Ejemplos Prácticos de Código

#### A. El Pipeline Completo e Ininterrumpido
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

#### B. Filtrado Dinámico de Filas (.loc con Lambdas)
```python
# Tienes un DataFrame con horas de juego, algunas nulas, y niveles.
# Queremos: rellenar horas nulas con la media, y filtrar jugadores con nivel >= 100 y horas > 50.
df_jugadores = pd.DataFrame({
    'jugador': ['Tarnished1', 'GutsBuild', 'AshenOne'],
    'nivel': [150, 120, 90],
    'horas_juego': [120.0, np.nan, 45.0]
})

df_veteranos = (df_jugadores
                .assign(horas_juego=lambda x: x['horas_juego'].fillna(x['horas_juego'].mean()))
                # ⚠️ Es obligatorio usar lambda x: ya que 'horas_juego' ha sido rellenada en el assign previo
                .loc[lambda x: (x['nivel'] >= 100) & (x['horas_juego'] > 50)])

print(df_veteranos)
#       jugador  nivel  horas_juego
# 0  Tarnished1    150        120.0
# 1   GutsBuild    120         82.5
```

### 🔗 Ejercicios para Practicar
*   **Pipeline de inventario:** [3.py - Completo](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py)
*   **Chaining condicional:** [5.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L27-L50)
*   **Filtrado dinámico en pipeline:** [4.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L37-L57) | [5.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L27-L50)
*   **Clientes VIP:** [11.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L76-L101)
*   **Mega-Pipeline de producción:** [12.py - Ejercicio 8](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L98-L115)
