# Simulaciones de Probabilidad - Parcial 4

**Integrantes:**  
* 👤 **Javier Alvarado** - Carné 24546  
* 👤 **Hugo Méndez** - Carné 241265  

---

Este proyecto contiene una colección de simulaciones escritas en Python. Las simulaciones abarcan problemas clásicos de probabilidad con dados, monedas, extracción de canicas y cartas de una baraja estándar.

---

## 📌 Requisitos y Configuración del Experimento

Para garantizar la reproducibilidad y el rigor estadístico de los resultados obtenidos, cada simulación cumple estrictamente con las siguientes directrices:
1. **Semilla Aleatoria:** Se fija la semilla del generador de números aleatorios en `2026` antes de realizar cualquier generación.
2. **Repeticiones:** Cada experimento se repite exactamente **10,000 veces**.
3. **Formato de Salida:** Las respuestas se muestran con una precisión de **cuatro decimales** (`.4f`).

---

## 🛠️ Descripción de las Simulaciones

### 🎲 Problema A - Dados (`problema_a.py`)
Simula el lanzamiento de dos dados justos de 6 caras.
* **Suma de 7:** Estima la probabilidad de que la suma de los dados sea exactamente igual a $7$.
* **Probabilidad Condicional:** Estima la probabilidad de que la suma sea $7$ dado que al menos uno de los dados obtuvo un valor par.
  * *Relación Teórica:* Todos los eventos posibles que suman 7 contienen al menos un número par, reduciendo el espacio muestral a 27 casos válidos.

### 🪙 Problema B - Monedas (`problema_b.py`)
Simula el lanzamiento de tres monedas justas de dos caras (cara o cruz).
* **Exactamente 2 Caras:** Estima la probabilidad de obtener exactamente dos caras en los tres lanzamientos.
* **Valor Esperado $E[X]$:** Sea $X$ la variable aleatoria que representa el número total de caras. Se calcula la media experimental de caras obtenidas en las 10,000 iteraciones para estimar $E[X]$.

### 🔴 Problema C - Canicas de Colores (`problema_c.py`)
Modelado de extracción de elementos sin reemplazo utilizando un enfoque basado en listas de muestras.
* **Caso Base:** Estima la probabilidad de extraer dos canicas rojas consecutivas de una caja que contiene 5 rojas, 3 azules y 2 verdes (total 10 canicas).
* **Caso de Dos Cajas:** Dadas la Caja 1 (5R, 3A, 2V) y la Caja 2 (2R, 5A, 3V), se selecciona una caja de manera equiprobable al azar y se extraen dos canicas sin reemplazo. Si el resultado es exactamente una roja y una verde, estima la probabilidad de que provengan de la Caja 1.

### 🃏 Problema D - Cartas de Baraja (`problema_d.py`)
Simula la extracción consecutiva y sin reemplazo de dos cartas de una baraja estándar de 52 cartas.
* **Ambas Ases:** Estima la probabilidad de extraer dos ases de forma consecutiva.
* **Análisis de Independencia:** Define los eventos $A$ (la primera carta es un As) y $B$ (la segunda carta es un As). Programa la evaluación de la independencia estadística comprobando la igualdad:
  $$P(A \cap B) \stackrel{?}{=} P(A) \cdot P(B)$$
  Dado que la extracción es sin reemplazo, el programa evalúa y demuestra que los eventos son **dependientes** (`False`).

---

## 📊 Tabla de Resultados (Semilla: 2026)

| Experimento / Métrica | Valor Simulado | Valor Teórico Exacto |
| :--- | :---: | :---: |
| **P(suma = 7)** | `0.1642` | $\frac{1}{6} \approx 0.1667$ |
| **P(suma = 7 \| al menos un par)** | `0.2174` | $\frac{2}{9} \approx 0.2222$ |
| **P(exactamente 2 caras)** | `0.3760` | $\frac{3}{8} = 0.3750$ |
| **E[X] (Número de caras)** | `1.5002` | $1.5000$ |
| **P(ambas rojas)** | `0.2249` | $\frac{2}{9} \approx 0.2222$ |
| **P(Caja 1 \| una roja y una verde)** | `0.6115` | $\frac{27}{44} \approx 0.6136$ *(Teórico exacto Bayes)* |
| **P(ambas ases)** | `0.0036` | $\frac{1}{221} \approx 0.0045$ |
| **P(A) * P(B)** | `0.0055` | $\frac{1}{169} \approx 0.0059$ |
| **¿Eventos A y B Independientes?** | `False` | `False` |

---

## 📂 Estructura del Repositorio

* `problema_a.py`: Módulo que contiene la función `simular_dados()`.
* `problema_b.py`: Módulo que contiene la función `simular_monedas()`.
* `problema_c.py`: Módulo que contiene la función `simular_canicas()`.
* `problema_d.py`: Módulo que contiene la función `simular_cartas()`.
* `simulaciones.ipynb`: Jupyter Notebook que importa, integra y ejecuta interactivamente las 4 funciones de simulación para observar los resultados organizados.

---

## 🚀 Cómo Ejecutar el Proyecto

### Clonar el proyecto: 

```bash
git clone https://github.com/hmndzzl/probs-parcial4.git
cd probs-parcial4
```

El proyecto está estructurado para que puedas ejecutarlo de forma interactiva y unificada a través del Jupyter Notebook **`simulaciones.ipynb`**, o bien llamando de forma individual a cada módulo.

### 📓 Ejecución interactiva con el Notebook (`simulaciones.ipynb`)
Abre el notebook interactivo utilizando un editor compatible (como VS Code, Google Colab o Jupyter Lab) y ejecuta las celdas de código. El notebook sirve como punto de integración importando y corriendo todos los experimentos.
