def imprimir_triangulo(n):
    """Dibuja un triángulo rectángulo de altura n."""
    for i in range(1, n + 1):
        print("*" * i)

def imprimir_cuadrado(n):
    """Dibuja un cuadrado de lado n."""
    for i in range(n):
        print("* " * n)

def imprimir_piramide(n):
    """Dibuja una pirámide centrada de altura n."""
    for i in range(1, n + 1):
        espacios = " " * (n - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)

def menu_patrones():
    """Menú para seleccionar patrones geométricos"""
    while True:
        print("\n--- PATRONES GEOMÉTRICOS ---")
        print("1. Triángulo")
        print("2. Cuadrado")
        print("3. Pirámide")
        print("4. Volver al menú principal")

        # Solicitar opción al usuario
        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "4":
            print("Regresando al menú principal...")
            break
        
        if opcion in ["1", "2", "3"]:
            try:
                # Pedir tamaño del patrón
                tamano = int(input("Ingrese el tamaño/altura del patrón: "))
                
                # Llamar a la función correspondiente
                if opcion == "1":
                    imprimir_triangulo(tamano)
                elif opcion == "2":
                    imprimir_cuadrado(tamano)
                elif opcion == "3":
                    imprimir_piramide(tamano)
                
                # Preguntar si desea ver otro patrón
                continuar = input("\n¿Desea ver otro patrón? (s/n): ").lower()
                if continuar != 's':
                    break
                    
            except ValueError:
                print("Error: Por favor, ingrese un número entero para el tamaño.")
        else:
            print("Opción no válida. Intente de nuevo.")

# Para probar el menú directamente
if __name__ == "__main__":
    menu_patrones()
