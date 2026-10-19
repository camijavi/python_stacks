# Stack Terminal Simulator Guide / Guía del Simulador de Pila en Terminal

---

## 🇬🇧 English Version

### 1. Overview
The **Stack Terminal Simulator** (`simulator.py`) is a pure Python visualizer designed to replicate the interactive memory diagram and step-through debugger of [Python Tutor](https://pythontutor.com/) directly inside the terminal.

It provides:
- A side-by-side **Frames and Objects** diagram of runtime memory.
- Pointer arrows tracking references between frames, classes, and instances.
- Stepping buttons (`<< First`, `< Prev`, `Next >`, `Last >>`) and a progress slider bar.
- Code line highlighting showing the executed line and the next line to run.

---

### 2. How to Run

You can launch the simulator in any of the following ways:

#### Option A: Run the main program
```bash
python3 main.py
```
This runs the stack operations and displays the interactive visualizer when `pila.print()` is reached.

#### Option B: Run the standalone simulator
```bash
python3 simulator.py
```
Starts stepping from Step 1 (`pila = Stack()`).

#### Option C: From your own Python code
```python
from stack import Stack, Producto

pila = Stack()
prod = Producto("P-01", "Mascarilla", 15.23, 6200)
pila.push(prod)

# Launch the visualizer:
pila.print()        # or pila.simulate()
```

---

### 3. Visual Layout Explained

The terminal screen is divided into 4 main sections:

#### A. Source Code Window (`main.py`)
Displays the executing code with Python Tutor arrows:
- `🟢 ➡ line that just executed`: Green arrow pointing to the line that just ran.
- `🔴 ➡ next line to execute`: Red arrow pointing to the upcoming line.

#### B. Memory Graph (Frames & Objects)
- **`Global frame`**: Displays the active global scope variables (`Producto`, `Stack`, `pila`, `prod`) with bullet dots `●` indicating references.
- **`Producto class` & `Stack class`**: Visualizes the class blueprints in memory.
- **`Stack instance`**: Shows the stack object with its `top │ ●` pointer.
- **`Producto instance` Nodes**: Linked together in memory:
  - The most recent item (`P-03`, TOP of the stack) is pointed to by `Stack.top`.
  - Its `next │ ●` pointer references the previous node (`P-02`).
  - `P-02.next │ ●` references the base node (`P-01`).
  - `P-01.next` is `None` (the bottom of the stack).

#### C. Progress Slider
```text
      ───────────────────────────⚪──────────────────
```
Represents current execution progress through a visual scrubber.

#### D. Navigation Buttons
```text
     ┌───────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
     │  << First │  │  < Prev  │  │  Next >  │  │  Last >> │
     └───────────┘  └──────────┘  └──────────┘  └──────────┘
                        Step 7 of 11
```

---

### 4. Interactive Keyboard Controls

| Key | Action | Description |
| :--- | :--- | :--- |
| <kbd>Enter</kbd> or <kbd>n</kbd> or <kbd>→</kbd> | **Next >** | Advances to the next execution step |
| <kbd>p</kbd> or <kbd>←</kbd> | **< Prev** | Steps back to the previous execution step |
| <kbd>f</kbd> or <kbd>Home</kbd> | **<< First** | Jumps directly to Step 1 |
| <kbd>l</kbd> or <kbd>End</kbd> | **Last >>** | Jumps directly to the final step |
| <kbd>q</kbd> | **Quit** | Exits the simulator and resumes execution |

---
---

## 🇪🇸 Versión en Español

### 1. Descripción General
El **Simulador de Pila en Terminal** (`simulator.py`) es un visualizador en Python puro diseñado para replicar fielmente el diagrama de memoria y los controles paso a paso de [Python Tutor](https://pythontutor.com/) directamente en la consola.

Incluye:
- Diagrama estructurado de **Frames (Marcos)** y **Objects (Objetos en memoria)**.
- Punteros y flechas que reflejan las referencias reales entre variables, clases e instancias.
- Botones de navegación interactiva (`<< First`, `< Prev`, `Next >`, `Last >>`) y barra de progreso deslizante (slider).
- Resaltado de código fuente indicando la línea recién ejecutada y la próxima por ejecutar.

---

### 2. Cómo Ejecutar

Puedes iniciar el simulador mediante cualquiera de las siguientes alternativas:

#### Opción A: Ejecutar el programa principal
```bash
python3 main.py
```
Ejecuta las operaciones de la pila y abre el simulador interactivo al llamar `pila.print()`.

#### Opción B: Ejecutar el simulador independiente
```bash
python3 simulator.py
```
Inicia la simulación desde el Paso 1 (`pila = Stack()`).

#### Opción C: Desde tu propio código en Python
```python
from stack import Stack, Producto

pila = Stack()
prod = Producto("P-01", "Mascarilla", 15.23, 6200)
pila.push(prod)

# Iniciar el simulador:
pila.print()        # o también: pila.simulate()
```

---

### 3. Explicación de los Componentes Visuales

La pantalla se organiza en 4 áreas principales:

#### A. Ventana de Código Fuente (`main.py`)
Muestra el código del programa con la simbología de Python Tutor:
- `🟢 ➡ line that just executed`: Flecha verde que indica la línea que se acaba de ejecutar.
- `🔴 ➡ next line to execute`: Flecha roja que indica la siguiente línea por ejecutar.

#### B. Diagrama de Memoria (Frames y Objetos)
- **`Global frame` (Marco global)**: Muestra las variables del alcance global (`Producto`, `Stack`, `pila`, `prod`) con puntos de referencia `●`.
- **`Producto class` y `Stack class`**: Muestran la definición de las clases en memoria con sus métodos.
- **`Stack instance` (Instancia de la pila)**: Muestra el objeto de la pila con su puntero `top │ ●`.
- **Nodos `Producto instance`**: Enlazados en memoria:
  - El elemento superior (`P-03`, TOP de la pila) es apuntado por `Stack.top`.
  - El puntero `next │ ●` de `P-03` apunta hacia arriba al nodo anterior (`P-02`).
  - El puntero `next │ ●` de `P-02` apunta hacia arriba al nodo base (`P-01`).
  - El atributo `next` de `P-01` es `None` (indica el fondo de la pila).

#### C. Barra Deslizante (Slider)
```text
      ───────────────────────────⚪──────────────────
```
Muestra de forma visual el avance del scrubber en la traza de ejecución.

#### D. Botones de Navegación
```text
     ┌───────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
     │  << First │  │  < Prev  │  │  Next >  │  │  Last >> │
     └───────────┘  └──────────┘  └──────────┘  └──────────┘
                        Step 7 of 11
```

---

### 4. Controles por Teclado

| Tecla | Acción | Descripción |
| :--- | :--- | :--- |
| <kbd>Enter</kbd> o <kbd>n</kbd> o <kbd>→</kbd> | **Next >** | Avanza al siguiente paso de ejecución |
| <kbd>p</kbd> o <kbd>←</kbd> | **< Prev** | Retrocede al paso de ejecución anterior |
| <kbd>f</kbd> o <kbd>Inicio</kbd> | **<< First** | Salta directamente al Paso 1 |
| <kbd>l</kbd> o <kbd>Fin</kbd> | **Last >>** | Salta directamente al último paso |
| <kbd>q</kbd> | **Salir** | Sale del simulador y continúa la ejecución del script |
