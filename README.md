# 📚 Guía de Clasificación Temática para Estudio: Python DAM

Este repositorio está clasificado para facilitar el estudio de patrones comunes en **Python Puro** y **Pandas**. A continuación encontrarás los ejercicios agrupados según la técnica o herramienta que utilizan.

---

## 📂 Clasificación de Ejercicios por Técnica de Estudio

### 🔑 1. Uso de Diccionarios y Estructuras Puras (Python Puro)
Ejercicios enfocados en crear, rellenar y anidar diccionarios, conteo de frecuencias, ordenaciones personalizadas y list/dict comprehensions.

*   **Frecuencia y conteo con diccionarios:**
    *   [1.py - Ejercicio 3 (Frecuencia de Caracteres)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L50): Uso de `.get(char, 0) + 1` para contar ocurrencias.
    *   [12.py - Ejercicio 1 (Auditoría de Logs)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L4): Clasificación y acumulación de conteos en un diccionario por ID.
*   **Diccionarios anidados y cálculos:**
    *   [1.py - Ejercicio 7 (Medias de Usuarios)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L118): Extraer datos numéricos de listas dentro de diccionarios anidados.
    *   [12.py - Ejercicio 2 (Consumo Eléctrico Anidado)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L22): Acceso seguro a claves secundarias `comp['specs']['w']`.
*   **List / Dict Comprehensions y Filtrado:**
    *   [1.py - Ejercicio 5 (Cuadrados Especiales)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L84): Generación y filtrado rápido de datos en una sola línea.
    *   [5.py - Ejercicio 1 (Hardware Entusiasta)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L4): Dict comprehension condicional `{k: v for ... if ...}`.
*   **Ordenación con lambdas:**
    *   [1.py - Ejercicio 4 (Ordenación de Tuplas)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L69): Ordenación multicriterio mediante tuplas inversas en la clave lambda.
    *   [11.py - Ejercicio 1 (Doble Criterio de Empleados)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L4): Combinación de ordenación de strings (ascendente) y números (descendente).

---

### 🧹 2. Uso de Limpieza y Formateo de Datos (Pandas & Python)
Ejercicios dedicados a quitar texto sucio, tratar valores nulos (`NaN` / `None`), transformar formatos numéricos/monetarios y validar tipos.

*   **Limpieza de Strings y Conversión de Texto a Número:**
    *   [6.py - Ejercicio 3 (Monedas Sucias)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L49): Limpieza de símbolos monetarios (`$`, `,`, `USD`) y conversión a flotante.
    *   [12.py - Ejercicio 4 (RAMs Sucias)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L54): Eliminación de sufijos "GB", normalización de texto y conversión.
*   **Imputación de Nulos (NaN):**
    *   [3.py - Parte 1 (Limpieza de Inventario)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21): Relleno de nulos con la mediana (`.fillna(df['col'].median())`) y casting con `.astype()`.
    *   [4.py - Ejercicio 2 (Historial de Jugadores)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L37): Limpieza selectiva y eliminación de filas con nulos críticos (`.dropna()`).
*   **Validación Estricta de Formato (Python Puro):**
    *   [2.py - Ejercicio 1 (Limpieza de JSON)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L3): Comprobación de tipos (`isinstance`) y patrones de texto en correos (`@` y `.`).
    *   [6.py - Ejercicio 1 (Procesamiento de Logs)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L4): Parsear strings estructurados con delimitadores mediante `.split()`.

---

### ⚠️ 3. Uso de Excepciones y Tolerancia a Fallos
Ejercicios que enseñan a evitar que un programa de producción falle por culpa de datos sucios o incoherencias operativas.

*   **Evitar Divisiones por Cero y Errores de Tipo:**
    *   [1.py - Ejercicio 6 (FPS y CPU)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L95): Inserción del texto `"ERROR"` en lugar de detener el bucle.
    *   [9.py - Ejercicio 1 (Cálculo de DPS)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L4): Captura múltiple de `ZeroDivisionError` y `TypeError` en listas paralelas.
*   **Lectura Segura de Diccionarios y Parámetros:**
    *   [4.py - Ejercicio 1 (Ventas por Categoría)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L4): Control de claves inexistentes y datos no numéricos mezclados.
    *   [9.py - Ejercicio 3 (Carga Segura de DataFrames)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L66): Lanzamiento de excepciones controladas si no existen columnas requeridas.
*   **Lógica defensiva en Pandas `.apply()`:**
    *   [9.py - Ejercicio 4 (Limpieza con Apply)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L88): Usar funciones personalizadas con bloques `try-except` fila a fila.

---

### 📊 4. Agrupaciones y Métricas (Group By & Aggregations)
Cómo clasificar registros por categorías y calcular estadísticas resumen como medias, sumas o conteos.

*   **Agrupaciones y Métricas Básicas:**
    *   [2.py - Ejercicio 4 (Videojuegos)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L94): Uso básico de `.groupby()` con métricas agregadas automáticas (`max`, `mean`).
    *   [4.py - Ejercicio 4 (Win Rate de Escuderías)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L86): Agrupación y renombrado implícito de agregaciones múltiples.
*   **Agrupaciones Multi-clave (Varios campos):**
    *   [5.py - Ejercicio 4 (Reporte Financiero)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L82): Agrupar por `departamento` y `tipo_gasto` simultáneamente.
*   **Aplanamiento de MultiIndex:**
    *   [10.py - Ejercicio 4 (Aplanamiento MultiIndex)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L67): Cómo unir nombres de columnas multinivel tras agregaciones complejas.
    *   [12.py - Ejercicio 6 (Reporte de Farmeo)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L77): Renombrar y aplanar índices multinivel para volver a un DataFrame regular.

---

### 🔗 5. Combinación y Cruce de Tablas (Merges & Joins)
Ejercicios sobre cómo realizar operaciones equivalentes a SQL `JOIN` y agrupaciones verticales de registros (`UNION ALL`).

*   **Left / Inner Joins:**
    *   [3.py - Parte 1 (Cruce Inventario)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21): Cruzar catálogos usando claves comunes con `how='left'`.
    *   [4.py - Ejercicio 3 (Evaluar Meta)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59): Realizar un `inner` merge y eliminar la clave sobrante.
    *   [12.py - Ejercicio 5 (Gestionar Entrenamiento)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66): Inner join con lógica condicional subsecuente.
*   **Concatenación Vertical (Concat):**
    *   [10.py - Ejercicio 2 (Unificación Mensual)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L34): Concatenar múltiples DataFrames con las mismas columnas usando `pd.concat()`.

---

### 🧠 6. Lógica Condicional y Mapeo (np.where, np.select, .map)
Técnicas para crear nuevas columnas basadas en condiciones complejas o diccionarios de equivalencias.

*   **Condiciones Binarias (`np.where`):**
    *   [4.py - Ejercicio 3 (Viabilidad Meta)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59): Clasificar registros en dos opciones.
    *   [5.py - Ejercicio 3 (Evaluación de Rendimiento)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L52): Condición de cumplimiento basándose en comparar dos columnas de datos.
*   **Mapeos mediante Diccionarios:**
    *   [12.py - Ejercicio 7 (Canales de Venta)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L89): Usar `.map(diccionario)` e imputar nulos con `"Otro"`.

---

### 📅 7. Series Temporales y Fechas
Ejercicios sobre el tratamiento de fechas, extracción de componentes de tiempo y cálculos de duración de eventos.

*   **Extracción de atributos de fecha:**
    *   [11.py - Ejercicio 2 (Reporte Mensual)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L30): Uso de `.dt.month` para agrupar ventas por mes calendario.
*   **Diferencias de Tiempo (Duraciones):**
    *   [12.py - Ejercicio 3 (Sesiones de Usuarios)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L37): Calcular minutos restando timestamps y aplicando `.dt.total_seconds() / 60`.

---

## ⚡ Method Chaining Extremo (Los ejercicios integradores)
Si buscas entrenar la escritura de código limpio y compacto en Pandas, estudia los siguientes ejercicios que ejecutan todo su flujo en una sola cadena de instrucciones:

1.  **[3.py - El simulacro de inventario](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py)**: Combina datos, limpia nulos, filtra y reporta en bloques encadenados.
2.  **[5.py - Ejercicio 2 (Stats de Training)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L27)**: Chaining extremo usando funciones lambdas para filtros intermedios.
3.  **[11.py - Ejercicio 4 (Clientes VIP)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L76)**: Creación de columnas de subtotal, agrupación, suma, filtro por total y ordenación en un solo paso.
4.  **[12.py - Ejercicio 8 (Mega-Pipeline)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L98)**: La prueba de fuego definitiva. Une dos DataFrames, calcula subtotales, agrupa, suma, filtra con `.loc` y ordena sin guardar variables intermedias.
