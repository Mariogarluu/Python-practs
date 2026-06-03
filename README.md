# 📚 Guía de Estudio y Cheatsheet: Python DAM

Este repositorio recopila una serie de ejercicios prácticos orientados al desarrollo en **Python Puro** y al análisis/manipulación de datos con **Pandas** para el módulo de Programación / Acceso a Datos de DAM (Desarrollo de Aplicaciones Multiplataforma).

---

## 🗺️ Mapa General del Repositorio

| Archivo | Nivel | Ejercicios | Enfoque Principal |
| :--- | :--- | :--- | :--- |
| 📄 [1.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py) | Básico | Ej. 1 al 8 | Lógica algorítmica, tipos primitivos, listas, diccionarios y control de excepciones básico. |
| 📄 [2.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py) | Básico-Medio | Ej. 1 al 4 | Limpieza manual en colecciones nativas y primeros pasos con DataFrames y agrupaciones Pandas. |
| 📄 [3.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py) | Integrador | Pipeline Completo | Un simulacro completo que encadena cruces de tablas (`merge`), limpieza (`fillna`), filtrado (`.loc`) y agregaciones. |
| 📄 [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py) | Medio | Ej. 1 al 4 | Tratamiento de diccionarios, filtros con condiciones booleanas compuestas y `.groupby().agg()`. |
| 📄 [5.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py) | Avanzado | Ej. 1 al 4 | Comprensión de diccionarios en una línea, encadenamiento de métodos extremo y `np.select`. |
| 📄 [6.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py) | Medio | Ej. 1 al 4 | Procesamiento de strings de texto (logs, monedas con símbolos) y conversiones de tipos. |
| 📄 [7.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py) | Medio | Ej. 1 al 4 | Mapeo de fechas con Pandas, probabilidades estadísticas aplicadas (gachas) y merges. |
| 📄 [8.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/8.py) | Medio-Avanzado | Ej. 1 al 3 | Procesamiento de metadatos de audio con Python y simulaciones de volumen/peso con Pandas. |
| 📄 [9.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py) | Avanzado | Ej. 1 al 4 | Tolerancia a fallos: cómo hacer que funciones y pipelines de Pandas nunca se detengan ante datos rotos. |
| 📄 [10.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py) | Avanzado | Ej. 1 al 4 | Aplanamiento de estructuras anidadas, concat, conteo de frecuencias de series y MultiIndex. |
| 📄 [11.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py) | Avanzado | Ej. 1 al 4 | Series temporales complejas con `.dt`, ordenaciones multicriterio avanzadas y la lógica VIP. |
| 📄 [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py) | Complejo | Ej. 1 al 8 | El recopilatorio definitivo de retos: desde análisis de logs puros hasta el Mega-Pipeline final. |

---

## 📖 Guía de Estudio Detallada (Estructura de Ejercicios)

A continuación, tienes el desglose de cada ejercicio con su propósito de estudio, los conceptos que entrena y los enlaces directos a sus correspondientes líneas de código.

### 📄 [1.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py) - Fundamentos de Python Puro
*   **[Ejercicio 1: Validación de Cadenas](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L1-L23)**
    *   **Propósito:** Validar que un string cumpla condiciones de seguridad (longitud entre 5 y 15, alfanumérico, primera letra alfabética).
    *   **Concepto clave:** Métodos de string `.isalnum()` y `.isalpha()`.
*   **[Ejercicio 2: Bucles y Lógica Matemática](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L24-L49)**
    *   **Propósito:** Filtrar números primos de una lista de enteros descartando tipos inválidos de forma segura.
    *   **Concepto clave:** Algoritmo de primalidad por raíz cuadrada (`num ** 0.5`) y `continue`.
*   **[Ejercicio 3: Frecuencia con Diccionarios](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L50-L68)**
    *   **Propósito:** Contar frecuencia de caracteres ignorando mayúsculas/minúsculas y espacios.
    *   **Concepto clave:** Inicialización defensiva de contadores usando `diccionario.get(clave, valor_por_defecto)`.
*   **[Ejercicio 4: Ordenación de Tuplas](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L69-L82)**
    *   **Propósito:** Ordenar armas por daño (descendente) y peso (ascendente en caso de empate).
    *   **Concepto clave:** `sorted(..., key=lambda x: (-x[1], x[2]))`.
*   **[Ejercicio 5: List Comprehensions](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L84-L94)**
    *   **Propósito:** Generar cuadrados de números pares divisibles por 3 entre el 1 y el 50 en una sola línea.
    *   **Concepto clave:** List comprehensions condicionales `[expr for x in seq if cond]`.
*   **[Ejercicio 6: Manejo de Excepciones](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L95-L117)**
    *   **Propósito:** Dividir FPS entre uso de CPU sin que detenga la ejecución si hay divisiones por cero o datos erróneos.
    *   **Concepto clave:** Bloque `try-except (ZeroDivisionError, TypeError)`.
*   **[Ejercicio 7: Diccionarios Anidados](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L118-L141)**
    *   **Propósito:** Calcular la nota media de usuarios de un diccionario donde los valores son listas con puntuaciones.
    *   **Concepto clave:** Iteración de claves y valores con `.items()`, control de listas vacías y redondeo `.round()`.
*   **[Ejercicio 8: Algoritmos Básicos](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L142-L155)**
    *   **Propósito:** Detectar palíndromos ignorando mayúsculas, espacios y signos de puntuación básicos.
    *   **Concepto clave:** Slicing inverso `[:: -1]` para invertir cadenas.

---

### 📄 [2.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py) - Primeros Pasos con Datos y Pandas
*   **[Ejercicio 1: Limpieza de JSON](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L3-L34)** (Python Puro)
    *   **Propósito:** Filtrar correos válidos (que contengan `@` y `.`) de usuarios mayores de edad.
    *   **Concepto clave:** Validación con `isinstance(x, list)` e `in` para subcadenas.
*   **[Ejercicio 2: Agrupación Manual](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L36-L74)** (Python Puro)
    *   **Propósito:** Calcular el salario medio de empleados agrupándolos manualmente por departamento.
    *   **Concepto clave:** Agrupación manual usando diccionarios cuyos valores son listas de números.
*   **[Ejercicio 3: Filtrado y Ordenación](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L76-L92)** (Pandas)
    *   **Propósito:** Seleccionar productos con stock y precio mayor a 50$, ordenándolos de mayor a menor precio.
    *   **Concepto clave:** Máscaras booleanas con el operador `&` y `.sort_values()`.
*   **[Ejercicio 4: Agrupación y Métricas](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L94-L109)** (Pandas)
    *   **Propósito:** Obtener la puntuación máxima y la media de reseñas por género de videojuego.
    *   **Concepto clave:** `.groupby('genero')['puntuacion'].agg(['max', 'mean'])`.

---

### 📄 [3.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py) - Simulacro: Pipeline de Gestión de Inventario
*   **[Parte 1: Combinación y Limpieza](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21-L35)**
    *   **Propósito:** Cruzar inventario con proveedores, renombrar columnas y rellenar valores faltantes (NaN).
    *   **Concepto clave:** `pd.merge(how='left')`, `.fillna()`, y `.astype(int)`.
*   **[Parte 2: Indexación y Mapeo](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L37-L51)**
    *   **Propósito:** Crear una columna de valor total y filtrar componentes que contengan "RTX" o "DDR5" con stock disponible.
    *   **Concepto clave:** Operadores booleanos de Pandas y `.str.contains()`.
*   **[Parte 3: Agrupación y Ordenamiento](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L53-L64)**
    *   **Propósito:** Generar un reporte de precio medio y stock total ordenado por volumen descendentemente.
    *   **Concepto clave:** `.groupby().agg()` pasándole argumentos con nombre personalizados.

---

### 📄 [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py) - Lógica Condicional y Pandas Medio
*   **[Ejercicio 1: Ventas por Categoría](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L4-L35)** (Python Puro)
    *   **Propósito:** Acumular ingresos totales por categoría a partir de un inventario sucio.
    *   **Concepto clave:** `try-except` anidados para manejar conversiones a `float` e `int` sobre datos corruptos.
*   **[Ejercicio 2: Jugadores Veteranos](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L37-L57)** (Pandas)
    *   **Propósito:** Limpiar horas jugadas nulas con la media y filtrar registros específicos usando exclusivamente `.loc`.
    *   **Concepto clave:** Filtrado mediante `df.dropna(subset=['col'])` y `.loc` con expresiones lambda.
*   **[Ejercicio 3: Evaluación de Viabilidad Meta](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59-L84)** (Pandas)
    *   **Propósito:** Unir personajes y clases para clasificar su viabilidad en base a su nivel/tier de poder.
    *   **Concepto clave:** `np.where()` para condiciones binarias (`Alta` vs `Normal`).
*   **[Ejercicio 4: Win Rate de Escuderías](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L86-L104)** (Pandas)
    *   **Propósito:** Calcular los puntos totales y porcentaje de victorias (win rate) por equipo deportivo.
    *   **Concepto clave:** Agrupación y mapeo directo con alias dentro de `.agg()`.

---

### 📄 [5.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py) - Method Chaining y Diccionarios
*   **[Ejercicio 1: Dict Comprehensions](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L4-L25)** (Python Puro)
    *   **Propósito:** Filtrar componentes de PC tipo RAM de baja latencia o GPU en una única línea de código.
    *   **Concepto clave:** `dictionary comprehension` combinado con expresiones condicionales complejas.
*   **[Ejercicio 2: Stats de Entrenamiento (Method Chaining)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L27-L50)** (Pandas)
    *   **Propósito:** En una única cadena, limpiar nombres, rellenar stamina, sumar velocidad y filtrar.
    *   **Concepto clave:** Chaining puro usando funciones anónimas `lambda x:` para referenciar el estado intermedio del DataFrame.
*   **[Ejercicio 3: Objetivos de Ventas](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L52-L80)** (Pandas)
    *   **Propósito:** Cruzar facturaciones de vendedores con sus metas y clasificarlos.
    *   **Concepto clave:** `pd.merge()` y `.drop(columns=[...])` en la misma cadena.
*   **[Ejercicio 4: Reporte Financiero de Gastos](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L82-L101)** (Pandas)
    *   **Propósito:** Agrupar datos por múltiples categorías (`departamento` y `tipo_gasto`) estimando totales y conteos.
    *   **Concepto clave:** Agrupaciones complejas Multi-key en Pandas.

---

### 📄 [6.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py) - Transformaciones de Texto y Strings
*   **[Ejercicio 1: Procesador de Logs](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L4-L33)** (Python Puro)
    *   **Propósito:** Analizar logs en formato "TIMESTAMP [NIVEL] MENSAJE" para contar errores por tipo.
    *   **Concepto clave:** Operaciones de string `.split()`, `.strip()` y control de errores por formateo incorrecto.
*   **[Ejercicio 2: Transformación de Logs a Tuplas](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L34-L48)** (Python Puro)
    *   **Propósito:** Convertir registros planos en una lista estructurada de tuplas.
    *   **Concepto clave:** Conversión rápida de datos y control de flujo.
*   **[Ejercicio 3: Conversión de Monedas Sucias](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L49-L72)** (Pandas)
    *   **Propósito:** Convertir strings de tipo `$1,200.00 USD` en valores float usables para cálculos matemáticos.
    *   **Concepto clave:** `.str.replace()` encadenado y `pd.to_numeric()`.
*   **[Ejercicio 4: Máximo Farmeo por Zona](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L73-L104)** (Pandas)
    *   **Propósito:** Obtener el personaje con más monedas en cada zona del juego.
    *   **Concepto clave:** `.groupby()`, `.idxmax()` e indexación por índice recuperado.

---

### 📄 [7.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py) - Gestión de Fechas e Incertidumbre (Gacha)
*   **[Ejercicio 1: Control de Presupuestos](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py#L4-L35)** (Python Puro)
    *   **Propósito:** Validar que los gastos de un proyecto no superen su presupuesto establecido.
    *   **Concepto clave:** Uso eficiente de diccionarios para cruzar ID de proyecto y coste.
*   **[Ejercicio 2: Parseo Seguro de Fechas](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py#L36-L58)** (Pandas)
    *   **Propósito:** Limpiar timestamps corruptos en publicaciones de redes sociales, descartando fechas rotas.
    *   **Concepto clave:** `pd.to_datetime(errors='coerce')` y filtrado con `.dropna()`.
*   **[Ejercicio 3: Simulador Gacha (Probabilidades)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py#L59-L82)** (Pandas)
    *   **Propósito:** Agrupar tiradas de un sistema aleatorio y calcular la probabilidad real de obtención.
    *   **Concepto clave:** Agrupaciones personalizadas y operaciones matemáticas elementales sobre agregaciones.
*   **[Ejercicio 4: Aggregations y Cruces](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py#L83-L104)** (Pandas)
    *   **Propósito:** Cruzar datos y extraer reportes de compras agregando por múltiples niveles.
    *   **Concepto clave:** `.groupby().agg()` y `.merge()` con alias.

---

### 📄 [8.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/8.py) - Ejercicios Intermedios-Avanzados
*   **[Ejercicio 1: Procesador de Catálogo de Audio](file:///c:/Users/mario/Desktop/Programacion/DAM/python/8.py#L4-L22)** (Python Puro)
    *   **Propósito:** Extraer la duración total y cantidad de pistas válidas por álbum en un catálogo musical.
    *   **Concepto clave:** Iteración anidada sobre diccionarios y listas de tracks.
*   **[Ejercicio 2: Análisis de Resina 3D](file:///c:/Users/mario/Desktop/Programacion/DAM/python/8.py#L23-L35)** (Pandas)
    *   **Propósito:** Calcular volumen total y consumo de resina en mililitros para impresiones 3D.
    *   **Concepto clave:** Operaciones aritméticas vectoriales en Pandas.
*   **[Ejercicio 3: Cruce de Datos de Usuarios](file:///c:/Users/mario/Desktop/Programacion/DAM/python/8.py#L36-L50)** (Pandas)
    *   **Propósito:** Unir perfiles de usuarios con sus estadísticas de actividad y limpiar campos incompletos.
    *   **Concepto clave:** `pd.merge()` y `.fillna()` con constantes.

---

### 📄 [9.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py) - Tolerancia Extrema a Fallos
*   **[Ejercicio 1: DPS Tolerante a Fallos](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L4-L34)** (Python Puro)
    *   **Propósito:** Calcular DPS (Daño por Segundo) con listas de daño y tiempos que contienen datos rotos (letras, ceros).
    *   **Concepto clave:** Captura de `ZeroDivisionError`, `TypeError` y `ValueError` de forma individual.
*   **[Ejercicio 2: Parseador de Logs de Sensores](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L35-L65)** (Python Puro)
    *   **Propósito:** Extraer lecturas de temperatura de un string continuo separando los campos válidos.
    *   **Concepto clave:** Parseo manual de strings con conversiones numéricas robustas.
*   **[Ejercicio 3: Interfaz Segura para Carga](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L66-L87)** (Pandas + Excepciones)
    *   **Propósito:** Cargar DataFrames y validar la existencia de columnas críticas antes de operar.
    *   **Concepto clave:** Programación defensiva levantando `KeyError` manuales.
*   **[Ejercicio 4: Limpieza Compleja con `.apply()`](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L88-L107)** (Pandas)
    *   **Propósito:** Limpiar valores numéricos mal formateados en un DataFrame usando lógica personalizada por fila.
    *   **Concepto clave:** Aplicación de funciones personalizadas usando `.apply()` y control de errores por celda.

---

### 📄 [10.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py) - Aplanamiento y MultiIndex
*   **[Ejercicio 1: Aplanador de JSON](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L4-L33)** (Python Puro)
    *   **Propósito:** Convertir estructuras de diccionarios profundamente anidados en diccionarios planos (clave_hijo).
    *   **Concepto clave:** Algoritmo recursivo para aplanamiento de JSON/diccionarios.
*   **[Ejercicio 2: Concatenación y Mapeo](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L34-L52)** (Pandas)
    *   **Propósito:** Concatenar múltiples DataFrames de registros mensuales de ventas y mapear los IDs de producto.
    *   **Concepto clave:** `pd.concat()` y `.map()` en Pandas.
*   **[Ejercicio 3: Frecuencias con Series](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L53-L66)** (Pandas + Python Puro)
    *   **Propósito:** Obtener la frecuencia absoluta de eventos y transformar el resultado en una Serie de Pandas estructurada.
    *   **Concepto clave:** Uso de `value_counts()` y wrappers.
*   **[Ejercicio 4: MultiIndex y Aplanamiento](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py#L67-L86)** (Pandas)
    *   **Propósito:** Resolver agrupaciones MultiIndex causadas por agregar múltiples funciones en varias columnas.
    *   **Concepto clave:** Comprensión de listas sobre `df.columns` para aplanar columnas multinivel.

---

### 📄 [11.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py) - Lógica de Negocio y Series Temporales
*   **[Ejercicio 1: Doble Criterio con Excepciones](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L4-L29)** (Python Puro)
    *   **Propósito:** Ordenar empleados por departamento (A-Z) y rendimiento (descendente) omitiendo nulos.
    *   **Concepto clave:** Ordenación doble invirtiendo signos en el parámetro `key=lambda x: (x['dep'], -x['rend'])`.
*   **[Ejercicio 2: Análisis Temporal](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L30-L53)** (Pandas)
    *   **Propósito:** Convertir fechas, quitar inválidas, extraer el número de mes e ingresos mensuales totales.
    *   **Concepto clave:** Accesor temporal `.dt.month` y agregación por unidad temporal.
*   **[Ejercicio 3: Cuota de Mercado Relativa](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L54-L75)** (Pandas)
    *   **Propósito:** Calcular el porcentaje de ingresos de cada canal sobre la suma total de ingresos de la empresa.
    *   **Concepto clave:** División por agregados acumulados: `x['ingresos'] / x['ingresos'].sum() * 100`.
*   **[Ejercicio 4: Clientes VIP (Method Chaining)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L76-L101)** (Pandas)
    *   **Propósito:** Encontrar clientes con gasto total > 500$ y ordenarlos de forma descendente en una sola expresión.
    *   **Concepto clave:** Method chaining estricto sin almacenar DataFrames intermedios.

---

### 📄 [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py) - Retos de Nivel Avanzado y Mega-Pipelines
*   **[Ejercicio 1: Auditoría de Logs de Errores](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L4-L21)** (Python Puro)
    *   **Propósito:** Contar cuántas veces aparece "ERROR" en registros planos tipo "ID-Accion-Estado".
    *   **Concepto clave:** Desempaquetado seguro y control de `IndexError` y `ValueError`.
*   **[Ejercicio 2: Consumo Eléctrico Anidado](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L22-L36)** (Python Puro)
    *   **Propósito:** Sumar los vatios ('w') de componentes cuyos specs están en diccionarios anidados.
    *   **Concepto clave:** Captura defensiva de `KeyError`, `TypeError` y `ValueError` al navegar diccionarios anidados.
*   **[Ejercicio 3: Tiempos de Sesión](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L37-L53)** (Pandas)
    *   **Propósito:** Calcular los minutos que dura una sesión comparando login y logout, filtrando las más largas.
    *   **Concepto clave:** Operación con deltas temporales y uso de `.dt.total_seconds() / 60`.
*   **[Ejercicio 4: Limpieza de RAMs Sucias](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L54-L65)** (Pandas)
    *   **Propósito:** Limpiar strings como "16 GB" o "32GB", convertirlos a número y rellenar fallos con 8.0.
    *   **Concepto clave:** Regex en Pandas con `.str.replace(r'\s*GB', '', regex=True)` y `pd.to_numeric()`.
*   **[Ejercicio 5: Mapeo de Estados de Stamina](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66-L76)** (Pandas)
    *   **Propósito:** Cruzar personajes con sus stats y asignar si entrenan o descansan según su stamina.
    *   **Concepto clave:** `pd.merge()` y clasificación con `np.where()`.
*   **[Ejercicio 6: Reporte de Farmeo (MultiIndex)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L77-L88)** (Pandas)
    *   **Propósito:** Agrupar derrotas de enemigos por zona y tipo, obteniendo el total y el máximo de almas recolectadas.
    *   **Concepto clave:** Redefinición y aplanamiento de columnas MultiIndex: `[f"{col}_{agg}" for col, agg in agrupado.columns]`.
*   **[Ejercicio 7: Mapeo con Canal por Defecto](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L89-L97)** (Pandas)
    *   **Propósito:** Traducir códigos de canales de venta a nombres usando un diccionario, asignando "Otro" si no existe.
    *   **Concepto clave:** Uso de `.map(diccionario)` y `.fillna({'col': 'Otro'})`.
*   **[Ejercicio 8: Mega-Pipeline de Producción](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L98-L115)** (Pandas)
    *   **Propósito:** El examen integrador final. Une pedidos y precios, calcula subtotales, agrupa por cliente, suma facturaciones, filtra a los VIP (>1000$) y los ordena descendentemente. Todo en una única línea/expresión.
    *   **Concepto clave:** Encadenamiento masivo de métodos en Pandas (`.merge().assign().groupby().agg().reset_index().loc[...].sort_values()`).

---

## 💡 Cheatsheet: Sintaxis Básica para el Examen

### Mapeos condicionales con Pandas
```python
import numpy as np

# 1. Condición simple binaria (np.where)
df['resultado'] = np.where(df['nota'] >= 5.0, 'Aprobado', 'Suspenso')

# 2. Múltiples condiciones (np.select)
condiciones = [
    df['edad'] < 18,
    df['edad'].between(18, 65),
    df['edad'] > 65
]
opciones = ['Menor', 'Adulto', 'Jubilado']
df['categoria'] = np.select(condiciones, opciones, default='Desconocido')
```

### Limpieza de datos rotos
```python
# Convertir columna a datetime forzando a NaT (Not a Time) si hay errores
df['fecha_limpia'] = pd.to_datetime(df['fecha_sucia'], errors='coerce')

# Convertir columna a numérico forzando a NaN si contiene letras
df['num_limpio'] = pd.to_numeric(df['num_sucio'], errors='coerce')

# Rellenar valores nulos por columna específica
df = df.fillna({'ram_limpia': 8.0, 'canal_nombre': 'Otro'})
```

### Aplanamiento de columnas tras un GroupBy con múltiples agregaciones
```python
agrupado = df.groupby(['zona', 'tipo'])[['almas']].agg(['sum', 'max'])
# Aplanamos la tupla (almas, sum) -> almas_sum
agrupado.columns = [f"{col}_{agg}" for col, agg in agrupado.columns]
agrupado = agrupado.reset_index()
```
