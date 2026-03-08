"""
Generador de Arte ASCII Animado
Proyecto de Animación

Equipo:
- Estudiante 1: [Nombre] - Menú y Patrones Geométricos
- Estudiante 2: [Nombre] - Generadores de Texto Artístico
- Estudiante 3: [Nombre] - Animaciones

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

# ============================================
# SECCIÓN 1: MENÚ PRINCIPAL (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú de la galería de arte ASCII"""
    print("\n" + "="*60)
    print("     🎨 GALERÍA DE ARTE ASCII v1.0 🎨")
    print("     Creado por: [El Ecuipo alfa dinamita omega masísa]")
    print("="*60)
    print("\nGALERÍA:")
    print("1. Patrones Geométricos")
    print("2. Generador de Banner")
    print("3. Marcos Decorativos")
    print("4. Animaciones")
    print("5. Tabla de Multiplicar Visual")
    print("6. Salir")
    print("-"*60)


# ============================================
# SECCIÓN 2: PATRONES GEOMÉTRICOS (Estudiante 1)
# ============================================

def triangulo(altura):
    """
    Genera un triángulo de asteriscos de altura especificada.

    Args:
        altura (int): Número de filas del triángulo
    """
    # TODO: Implementar
    # Usar un loop for con range(1, altura + 1)
    # Cada fila debe tener i asteriscos
    # Ejemplo: si altura=5
    # *
    # **
    # ***
    # ****
    # *****

    pass  # Reemplazar con su código


def cuadrado(lado):
    """
    Genera un cuadrado con bordes de tamaño especificado.

    Args:
        lado (int): Tamaño del lado del cuadrado
    """
    # TODO: Implementar
    # - Primera fila: todos asteriscos o símbolos
    # - Filas del medio: símbolo, espacios, símbolo
    # - Última fila: todos asteriscos o símbolos
    # Ejemplo: cuadrado(5)
    # *****
    # *   *
    # *   *
    # *   *
    # *****

    pass  # Reemplazar con su código


def piramide(altura):
    """
    Genera una pirámide centrada de altura especificada.

    Args:
        altura (int): Número de filas de la pirámide
    """
    # TODO: Implementar
    # Cada fila debe:
    # - Tener espacios al inicio para centrar: (altura - i) espacios
    # - Tener asteriscos: 2*i - 1 asteriscos
    # Ejemplo: piramide(5)
    #     *
    #    ***
    #   *****
    #  *******
    # *********

    pass  # Reemplazar con su código


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


# ============================================
# SECCIÓN 3: TEXTO ARTÍSTICO (Estudiante 2)
# ============================================

def generar_banner(texto):
    """Genera un banner con el texto ingresado."""
    linea = "═" * (len(texto) + 4)
    print(f"╔{linea}╗")
    print(f"║  {texto.upper()}  ║")
    print(f"╚{linea}╝")


def marco_decorativo(texto, estilo):
    """
    Crea un marco decorativo alrededor del texto.
    Estilo 1: Elegante (═ ║)
    Estilo 2: Estelar (★ ☆)
    """
    largo = len(texto)
    
    if estilo == 1:
        print(f"╔{'═' * (largo + 4)}╗")
        print(f"║  {texto}  ║")
        print(f"╚{'═' * (largo + 4)}╝")
    
    elif estilo == 2:
        borde = "★ ☆ " * ((largo // 4) + 2)
        print(borde)
        print(f"☆  {texto}  ★")
        print(borde)
    else:
        print("Estilo no reconocido.")


def tabla_multiplicar_visual(numero):
    """Genera una tabla de multiplicar con formato visual atractivo."""
    titulo = f"TABLA DEL {numero}"
    ancho_interno = 20  # Espacio suficiente para que se vea bien
    
    # 1. Crear encabezado decorativo
    print(f"\n╔{'═' * (ancho_interno + 2)}╗")
    print(f"║{titulo.center(ancho_interno + 2)}║")
    print(f"╠{'═' * (ancho_interno + 2)}╣")
    
    # 2. Generar tabla del 1 al 10 y 3. Alinear números correctamente
    for i in range(1, 11):
        resultado = numero * i
        # Usamos :2d para que el multiplicador y el resultado siempre ocupen el mismo espacio
        linea = f"{numero} x {i:>2} = {resultado:>3}"
        print(f"║  {linea.center(ancho_interno)}  ║")
    
    # 4. Cerrar con pie decorativo
    print(f"╚{'═' * (ancho_interno + 2)}╝")


def menu_texto_artistico():
    """Menú para generadores de texto artístico"""
    while True:
        print("\n--- GENERADORES DE TEXTO ---")
        print("1. Crear Banner")
        print("2. Marco Decorativo")
        print("3. Tabla de Multiplicar")
        print("4. Volver al menú principal/Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            txt = input("Ingrese el texto para su banner: ")
            generar_banner(txt)
            
        elif opcion == "2":
            txt = input("Ingrese el texto a enmarcar: ")
            print("Estilos: 1 (Elegante ═), 2 (Estrellas ★)")
            est = int(input("Elija estilo: "))
            marco_decorativo(txt, est)
            
        elif opcion == "3":
            try:
                num = int(input("¿De qué número desea la tabla? (1-10): "))
                tabla_multiplicar_visual(num)
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

# Ejecución del programa
if __name__ == "__main__":
    menu_texto_artistico()


# ============================================
# SECCIÓN 4: ANIMACIONES (Estudiante 3)
# ============================================

def crear_retraso(duracion):
    """
    Crea un retraso usando un loop vacío.

    Args:
        duracion (int): Factor de duración (más alto = más lento)
    """
    # TODO: Implementar retraso
    # Usar un loop for que no haga nada
    # Ejemplo: for _ in range(duracion * 100000):
    #              pass

    pass  # Reemplazar con su código


def barra_progreso():
    """Muestra una barra de progreso animada"""
    # TODO: Implementar barra de progreso
    # - Usar un loop de 0 a 100
    # - En cada iteración, mostrar la barra actualizada
    # - Usar caracteres como █ ■ o # para la barra llena
    # - Usar - o espacio para la parte vacía
    # - Mostrar el porcentaje

    # Ejemplo de salida:
    # Procesando...
    # [■■■■■■■■■■----------] 50%
    # [■■■■■■■■■■■■■■■■----] 80%
    # [■■■■■■■■■■■■■■■■■■■■] 100% ¡Completo!

    # Pista: usar end="\r" en print para sobrescribir la misma línea

    pass  # Reemplazar con su código


def animacion_texto_movil():
    """Anima un texto moviéndose de izquierda a derecha"""
    # TODO: Implementar animación de texto
    # - Definir el texto a animar
    # - Usar un loop para cada posición
    # - En cada iteración, imprimir espacios + texto
    # - Incrementar los espacios para simular movimiento
    # - Limpiar la línea anterior con \r

    # Ejemplo:
    # ☆                (frame 1)
    #  ☆               (frame 2)
    #   ☆              (frame 3)
    # ...

    pass  # Reemplazar con su código


def menu_animaciones():
    """Menú para animaciones"""
    print("\n--- ANIMACIONES ---")
    print("1. Barra de Progreso")
    print("2. Texto en Movimiento")
    print("3. Volver al menú principal")

    # TODO: Implementar lógica del menú

    pass  # Reemplazar con su código


# ============================================
# FUNCIONES AUXILIARES
# ============================================

def limpiar_pantalla_simple():
    """Imprime líneas en blanco para simular limpieza de pantalla"""
    # No usamos os.system() porque no está en los módulos 1-6
    print("\n" * 50)


def pausar():
    """Pausa hasta que el usuario presione Enter"""
    input("\nPresione Enter para continuar...")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔════════════════════════════════════════════════════════════╗")
    print("║           ¡Bienvenido a la Galería de Arte ASCII!         ║")
    print("║                                                            ║")
    print("║    Donde la creatividad se encuentra con la programación  ║")
    print("╚════════════════════════════════════════════════════════════╝")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_patrones()
        elif opcion == "2":
            print("\n--- GENERADOR DE BANNER ---")
            # TODO: Solicitar texto y generar banner
            pass
        elif opcion == "3":
            menu_texto_artistico()
        elif opcion == "4":
            menu_animaciones()
        elif opcion == "5":
            print("\n--- TABLA DE MULTIPLICAR VISUAL ---")
            # TODO: Solicitar número y generar tabla
            pass
        elif opcion == "6":
            print("\n" + "="*60)
            print("  ¡Gracias por visitar la Galería de Arte ASCII!")
            print("  Creado con ❤️  y código por: [Nombres del equipo]")
            print("="*60)
            continuar = False
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

        if continuar and opcion != "6":
            pausar()

    print("\nPrograma terminado. ¡Hasta pronto! 🎨")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
