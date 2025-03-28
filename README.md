# 🔢 Sistema de Búsqueda de Números Primos Especiales

Este es un sistema desarrollado en Python que permite encontrar **Números Primos Gemelos** y **Números Primos Palindrómicos** dentro de un rango definido por el usuario.

## 🌟 Características Principales

### 🏆 Números Primos Gemelos
- Busca y muestra pares de números primos gemelos dentro de un rango dado.
- Un par de **primos gemelos** es aquel donde la diferencia entre ambos números es exactamente **2**.
- Ejemplo: **(3,5)**, **(11,13)**, **(17,19)**.

### 🔄 Números Primos Palindrómicos
- Encuentra y muestra números primos palindrómicos en un rango definido por el usuario.
- Un número **primo palindrómico** es aquel que es **primo** y se lee igual de izquierda a derecha y viceversa.
- Ejemplo: **131**, **757**, **929**.

### 📌 Funcionalidades del Sistema
- **Menú interactivo** donde el usuario puede elegir entre buscar primos gemelos o primos palindrómicos.
- **Búsqueda eficiente** en rangos personalizados.
- **Implementación modular** para un código limpio y estructurado.
- **Mensajes claros** y formato intuitivo para facilitar la interacción.

## 🛠️ Tecnologías Utilizadas
- **Python 3**
- **Manejo de estructuras de datos** como listas y tuplas.
- **Lógica de números primos y palíndromos**.

## 📋 Requisitos
- Python 3.6 o superior.

## 🚀 Instalación y Uso
1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/NumerosPrimosEspeciales.git
    ```
2. Ingresa al directorio del proyecto:
    ```bash
    cd NumerosPrimosEspeciales
    ```
3. Ejecuta el programa:
    ```bash
    python main.py
    ```

## 📁 Estructura del Proyecto
```
NumerosPrimosEspeciales/
├── main.py                      # Menú principal
├── modulos/
│   ├── primos_gemelos.py         # Lógica para encontrar primos gemelos
│   ├── primos_palindromicos.py   # Lógica para encontrar primos palindrómicos
│   └── utils.py                  # Funciones auxiliares
└── README.md                     # Documentación del proyecto
```

### 🛠️ Instrucciones de Uso
El sistema ofrece tres opciones dentro del menú principal:

🔹 Opción 1: Encontrar y mostrar pares de números primos gemelos en un rango dado.
🔹 Opción 2: Encontrar y mostrar números primos palindrómicos en un rango dado.
🔹 Opción 3: Salir del programa.

📌 El usuario debe ingresar el límite superior del rango de búsqueda:

Para primos gemelos, el rango será (2, límite).

Para primos palindrómicos, el rango será (10, límite).



### ··🖥️ Código Principal (main.py) 
```
from modulos.primos_gemelos import primos_gemelos
from modulos.primos_palindromicos import primos_palindromicos

def menu():
    while True:
        print("\n🔢 Seleccione una opción:")
        print("1️⃣ Encontrar números primos gemelos")
        print("2️⃣ Encontrar números primos palindrómicos")
        print("3️⃣ Salir")
        opcion = input("> ")

        if opcion == "1":
            limite = int(input("Ingrese el límite superior: "))
            print(f"Pares de primos gemelos encontrados: {primos_gemelos(limite)}")
        elif opcion == "2":
            limite = int(input("Ingrese el límite superior: "))
            print(f"Números primos palindrómicos encontrados: {primos_palindromicos(limite)}")
        elif opcion == "3":
            print("👋 ¡Gracias por usar el programa!")
            break
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
```

### 🏆 Módulo de Primos Gemelos (primos_gemelos.py)
```
def es_primo(n):
    """Verifica si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_gemelos(rango):
    """Encuentra pares de primos gemelos dentro del rango dado."""
    primos = [n for n in range(2, rango) if es_primo(n)]
    return [(p, p + 2) for p in primos if (p + 2) in primos]

```

### 🔄 Módulo de Primos Palindrómicos (primos_palindromicos.py)

```
def es_palindromo(n):
    """Verifica si un número es palindrómico."""
    return str(n) == str(n)[::-1]

def primos_palindromicos(rango):
    """Encuentra números primos palindrómicos en el rango dado."""
    return [n for n in range(10, rango) if es_primo(n) and es_palindromo(n)]
```

### 📝 Ejemplo de Uso

Seleccione una opción:
1. Encontrar números primos gemelos
2. Encontrar números primos palindrómicos
3. Salir
> 1
Ingrese el límite superior: 50
Pares de primos gemelos encontrados: (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)

-----

### 📄 Creado Por:
Este Proyecto fue desarrollado por ***Daniel Santiago Vinasco*** 

-------------------------------------------------------


---
✅ ¿Qué incluye este README? :

✔ 🔢 Funcionalidades clave para encontrar números primos gemelos y palindrómicos.
✔ 📁 Estructura del proyecto organizada y modular.
✔ 🖥️ Código del menú principal con opciones interactivas.
✔ 🔎 Algoritmos eficientes para detectar números primos y palíndromos.
✔ 🚀 Instrucciones detalladas para instalación y uso del sistema.
✔ 🎨 Presentación atractiva con emojis y formato Markdown limpio.

----------------
