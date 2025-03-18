from modulos.primos import encontrar_primos_gemelos #importamos la función encontrar_primos_gemelos
from modulos.palindromos import encontrar_primos_palindromicos #importamos la función encontrar_primos_palindromicos

def mostrar_menu(): #definimos la función mostrar_menu
    while True:
        print("\n **************Bienvenidos al programa de números primos***********")
        print("\n🔢🔢🔢 Números Primos 🔢🔢🔢")
        print("\nSeleccione una opción:")
        print(" 1️⃣ 1. Encontrar números primos gemelos")
        print(" 2️⃣ 2. Encontrar números primos palindrómicos")
        print(" 3️⃣ 3. Salir - Cerrar el programa - Bye Bye")

        opcion = input("> ").strip() #pedimos al usuario que ingrese una opción

        if opcion == "1": #si la opción es 1
            try: #intentamos
                limite = int(input("Ingrese el límite superior: ").strip()) #pedimos al usuario que ingrese el límite superior
                gemelos = encontrar_primos_gemelos(limite) #llamamos a la función encontrar_primos_gemelos
                print("Pares de primos gemelos encontrados:", ", ".join(map(str, gemelos))) #imprimimos los pares de primos gemelos
            except ValueError:  #si hay un error
                print("❌ Error: Ingrese un número entero válido.") #imprimimos un mensaje de error

        elif opcion == "2": #si la opción es 2 
            try:
                limite = int(input("Ingrese el límite superior: ").strip()) #pedimos al usuario que ingrese el límite superior
                palindromos = encontrar_primos_palindromicos(limite)  #llamamos a la función encontrar_primos_palindromicos 

                if palindromos: #si hay palíndromos 
                    print("Números primos palindrómicos encontrados:", ", ".join(map(str, palindromos))) #imprimimos los números primos palindrómicos
                else: #si no hay palíndromos
                    print("No se encontraron números primos palindrómicos en este rango.") #imprimimos un mensaje
            except ValueError: #si hay un error
                print("❌ Error: Ingrese un  número entero válido.") #imprimimos un mensaje de error

        elif opcion == "3": #si la opción es 3
            print("Saliendo del programa...") #imprimimos un mensaje
            break

        else:
            print("❌ Opción no válida, intente de nuevo.") #imprimimos un mensaje de error

































