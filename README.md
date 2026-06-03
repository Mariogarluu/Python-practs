# 📚 Python DAM - Catálogo de Ejercicios y Cheatsheet

Repositorio con ejercicios prácticos resueltos en **Python Puro** y **Pandas** para el módulo de Programación / Acceso a Datos de DAM (Desarrollo de Aplicaciones Multiplataforma).

---

## 🔍 Índice Rápido de Archivos

| Archivo | Nivel / Tipo | Ejercicios Contenidos | Temas Clave |
| :--- | :--- | :--- | :--- |
| 📄 [1.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py) | Básico | Ejercicios 1 - 8 | Cadenas, Bucles, List Comprehensions, Diccionarios, Excepciones |
| 📄 [2.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py) | Básico-Medio | Ejercicios 1 - 4 | Limpieza JSON, Promedios Manuales, Pandas Intro, GroupBy |
| 📄 [3.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py) | Integrador | Pipeline Integral | Merge, Renombrado, Limpieza NaN, Indexación `.loc`, Reportes |
| 📄 [4.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py) | Medio | Ejercicios 1 - 4 | Excepciones, Indexación Avanzada, Cruces Condicionales, `.agg()` |
| 📄 [5.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py) | Avanzado | Ejercicios 1 - 4 | Dict Comprehension, Method Chaining Extremo, `np.select`, GroupBy |
| 📄 [6.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py) | Medio | Ejercicios 1 - 4 | Parsing de Logs, Conversión de Tipos, Limpieza de Strings Monetarios |
| 📄 [7.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py) | Medio | Ejercicios 1 - 4 | Presupuestos, Parseo de Fechas, Probabilidades Gacha, Cruces |
| 📄 [8.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/8.py) | Medio-Avanzado | Ejercicios 1 - 3 | Catálogo de Audio, Resina 3D, Cruce de Datos de Usuarios |
| 📄 [9.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py) | Avanzado | Ejercicios 1 - 4 | Cálculo DPS, Parsing logs hardware, Interfaz segura pandas, apply |
| 📄 [10.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/10.py) | Avanzado | Ejercicios 1 - 4 | Aplanamiento JSON, Concat, Frecuencias Series, MultiIndex |
| 📄 [11.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py) | Avanzado | Ejercicios 1 - 4 | Ordenación Multicriterio, Series Temporales, Métricas Relativas |
| 📄 [12.py](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py) | Complejo | Ejercicios 1 - 8 | Consumo eléctrico, Tiempos de sesión, np.where, Mega-Pipeline |

---

## 🛠️ Cheatsheet Temático (¿Dónde encuentro cada cosa?)

### 1. Python Estándar / Puro (Estructuras de Datos y Algoritmos)
* **Validación de Cadenas:**
  * [1.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L1-L22): Validación de usuario (longitud, alfanumérico, inicio con letra).
  * [1.py - Ejercicio 8](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L142-L155): Algoritmo para verificar palíndromos (limpieza de caracteres).
* **Colecciones y Diccionarios:**
  * [1.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L50-L68): Contar frecuencia de caracteres usando diccionarios.
  * [1.py - Ejercicio 7](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L118-L141): Cálculo de medias en diccionarios anidados.
  * [2.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L3-L34): Limpieza de lista de diccionarios (JSON) y extracción de correos válidos.
  * [2.py - Ejercicio 2](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L36-L74): Agrupación manual de tuplas para calcular promedios salariales.
  * [5.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L4): Filtrado avanzado usando Dict Comprehensions.
* **Ordenación y Lógica:**
  * [1.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L69-L82): Ordenación multicriterio de tuplas (daño descendente, peso ascendente).
  * [1.py - Ejercicio 5](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L84-L94): Cuadrados especiales con List Comprehensions filtrados.
  * [11.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/11.py#L4): Ordenación avanzada multicriterio con excepciones.

### 2. Gestión de Errores y Excepciones
* **Tratamiento seguro de datos:**
  * [1.py - Ejercicio 6](file:///c:/Users/mario/Desktop/Programacion/DAM/python/1.py#L95-L117): Manejo de `ZeroDivisionError` y `TypeError` en operaciones vectoriales.
  * [9.py - Ejercicio 1](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L4): Cálculo de DPS controlando divisiones por cero y tipos erróneos.
  * [9.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/9.py#L66): Interfaz segura para cargar y transformar dataframes controlando fallos.

### 3. Pandas - Transformación y Limpieza de Datos
* **Limpieza de Nulos (NaN) y Tipos:**
  * [3.py (Parte 1)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21-L35): Imputación de nulos con la mediana y conversión a `int`.
  * [6.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/6.py#L49): Limpieza y parseo de strings con formato monetario (ej: `$1,200.50` a flotante).
  * [12.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L54): Limpieza de texto numérico sucio (ej: "16 GB" -> 16.0).
* **Indexación y Selección Condicional:**
  * [2.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L76-L92): Filtrado simple con operadores lógicos (`&`) y ordenamiento.
  * [3.py (Parte 2)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L37-L51): Indexación avanzada con `.loc`, regex en strings (`str.contains`) y cálculo de columnas.
  * [5.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/5.py#L52): Uso de `np.select` para asignar categorías complejas por condiciones.
  * [12.py - Ejercicio 5](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L66): Empleo de `np.where` para mapeo condicional.

### 4. Pandas - Agrupaciones y Operaciones Cruzadas (Aggregations & Joins)
* **Agrupación y Métricas:**
  * [2.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/2.py#L94-L109): Agrupación simple con métricas agregadas (`max` y `mean`).
  * [3.py (Parte 3)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L53-L64): Agrupación y agregación con renombrado implícito.
  * [4.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L86): Agregaciones múltiples y específicas por columna.
  * [12.py - Ejercicio 6](file:///c:/Users/mario/Desktop/Programacion/DAM/python/12.py#L77): Agrupaciones complejas y aplanamiento de índices MultiIndex.
* **Cruce de Tablas (Merges):**
  * [3.py (Parte 1)](file:///c:/Users/mario/Desktop/Programacion/DAM/python/3.py#L21-L35): Cruce `left` básico entre tablas de inventario y proveedores.
  * [4.py - Ejercicio 3](file:///c:/Users/mario/Desktop/Programacion/DAM/python/4.py#L59): Combinación de dataframes y mapeo condicional de datos.
  * [7.py - Ejercicio 4](file:///c:/Users/mario/Desktop/Programacion/DAM/python/7.py#L83): Cruces complejos con agregaciones posteriores.

---

## 📈 Buenas Prácticas e Hilo Conductor
Cada solución busca aplicar principios limpios de desarrollo:
1. **Validación Exhaustiva:** Comprobar tipos de datos de entrada (`isinstance`) antes de procesar.
2. **Method Chaining:** En Pandas, concatenar métodos usando paréntesis para mantener el código legible y libre de variables intermedias innecesarias.
3. **Manejo de Nulos:** Evitar la propagación de nulos (`NaN` o `None`) usando imputaciones inteligentes (`fillna`, `.median()`).
