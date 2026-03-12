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

import os


HISTORIAL = []
RUTA_BASE = os.path.dirname(__file__)
RUTA_DATOS = os.path.join(RUTA_BASE,"datos")
GALERIA_ARCHIVO = os.path.join(RUTA_BASE,"datos","galeria.txt")

# ============================================
# SECCIÓN 1: MENÚ PRINCIPAL (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú de la galería de arte ASCII"""
    print("\n" + "="*60)
    print("     🎨 GALERÍA DE ARTE ASCII v1.0 🎨")
    print("     Creado por: Perla, Miguel, Ariel, Martha")
    print("="*60)
    print("\nGALERÍA:")
    print("1. Patrones Geométricos")
    print("2. Generador de Banner")
    print("3. Marcos Decorativos")
    print("4. Animaciones")
    print("5. Tabla de Multiplicar Visual")
    print("6. Salir")
    print("-"*60)

while True:
    mostrar_menu_principal()
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("Mostrando Patrones Geométricos...")
    elif opcion == "2":
        print("Generador de Banner...")
    elif opcion == "3":
        print("Marcos Decorativos...")
    elif opcion == "4":
        print("Animaciones...")
    elif opcion == "5":
        print("Tabla de Multiplicar Visual...")
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")

    input("\nPresiona Enter para volver al menú...")


# ============================================
# SECCIÓN 2: PATRONES GEOMÉTRICOS (Estudiante 1)
# ============================================

def triangulo(altura):
    """
    Genera un triángulo de asteriscos de altura especificada.

    Args:
        altura (int): Número de filas del triángulo.
        
    Returns:
        str: El arte ASCII del triángulo generado con saltos de línea.
    """
    # Inicializamos el string vacío para acumular el dibujo
    resultado = ""
    # Usar un loop for con range(1, altura + 1)
    for i in range(1, altura + 1):
        # Cada fila debe tener i asteriscos
        resultado += "*" * i + "\n"
    return resultado
    pass  


def cuadrado(lado):
    """
    Genera un cuadrado con bordes de tamaño especificado.

    Args:
        lado (int): Tamaño del lado del cuadrado.
        
    Returns:
        str: El arte ASCII del cuadrado hueco.
    """
    # Caso base para evitar errores con tamaños menores a 1
    if lado < 1: return ""
    if lado == 1: return "*\n"
    
    # - Primera fila: todos asteriscos o símbolos
    superior = "*" * lado + "\n"
    
    # - Filas del medio: símbolo, espacios, símbolo
    medio = ""
    for _ in range(lado - 2):
        medio += "*" + " " * (lado - 2) + "*" + "\n"
    
    # - Última fila: todos asteriscos o símbolos
    inferior = "*" * lado + "\n"
    
    return superior + medio + inferior

    pass  

def piramide(altura):
   """
    Genera una pirámide centrada de altura especificada.

    Args:
        altura (int): Número de filas de la pirámide.
        
    Returns:
        str: El arte ASCII de la pirámide centrada.
    """
    resultado = ""
    # Iteramos por cada nivel de la pirámide
    for i in range(1, altura + 1):
        # - Tener espacios al inicio para centrar: (altura - i) espacios
        espacios = " " * (altura - i)
        # - Tener asteriscos: 2*i - 1 asteriscos
        asteriscos = "*" * (2 * i - 1)
        resultado += espacios + asteriscos + "\n"
    return resultado

    pass  


def menu_patrones():
    """Menú para seleccionar patrones geométricos"""
    print("\n--- PATRONES GEOMÉTRICOS ---")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Pirámide")
    print("4. Volver al menú principal")

    # TODO: Implementar lógica del menú
    # - Solicitar opción al usuario
    # - Pedir tamaño del patrón
    # - Llamar a la función correspondiente
    # - Preguntar si desea ver otro patrón

    pass  # Reemplazar con su código


# ============================================
# SECCIÓN 3: TEXTO ARTÍSTICO (Estudiante 2)
# ============================================

def generar_banner(texto):
    """
    Genera un banner con el texto ingresado.

    Args:
        texto (str): Texto a convertir en banner
    """
    # TODO: Implementar banner grande
    # Opción simple: crear un marco alrededor del texto
    # Opción avanzada: convertir cada letra a ASCII art grande

    # Ejemplo simple:
    # ╔══════════════════════╗
    # ║                      ║
    # ║     HOLA MUNDO       ║
    # ║                      ║
    # ╚══════════════════════╝

    pass  # Reemplazar con su código


def marco_decorativo(texto, estilo):
    """
    Crea un marco decorativo alrededor del texto.

    Args:
        texto (str): Texto a enmarcar
        estilo (int): Tipo de estilo (1, 2, o 3)
    """
    # TODO: Implementar diferentes estilos de marcos
    # Estilo 1: Simple con ═ ║
    # Estilo 2: Doble con bordes decorativos
    # Estilo 3: Con asteriscos o caracteres especiales

    # Caracteres útiles:
    # ═ ║ ╔ ╗ ╚ ╝ (estilo 1)
    # ★ ☆ (estilo 2)
    # * # @ (estilo 3)

    pass  # Reemplazar con su código


def tabla_multiplicar_visual(numero):
    """
    Genera una tabla de multiplicar con formato visual atractivo.

    Args:
        numero (int): Número para generar la tabla (1-10)
    """
    # TODO: Implementar tabla decorada
    # - Crear encabezado decorativo
    # - Generar tabla del 1 al 10
    # - Alinear números correctamente
    # - Cerrar con pie decorativo

    # Ejemplo:
    # ╔════════════════════════╗
    # ║  TABLA DEL 5           ║
    # ╠════════════════════════╣
    # ║  5 x  1 =  5           ║
    # ║  5 x  2 = 10           ║
    # ║  ...                   ║
    # ╚════════════════════════╝

    pass  # Reemplazar con su código


def menu_texto_artistico():
    """Menú para generadores de texto artístico"""
    print("\n--- GENERADORES DE TEXTO ---")
    print("1. Crear Banner")
    print("2. Marco Decorativo")
    print("3. Tabla de Multiplicar")
    print("4. Volver al menú principal")

    # TODO: Implementar lógica del menú

    pass  # Reemplazar con su código


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
    for _ in range(duracion * 100000):
        pass


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

    print("Procesando...")
    total_bloques = 20
    for porcentaje in range(0, 101, 5):
        bloques_llenos = porcentaje * total_bloques // 100
        bloques_vacios = total_bloques - bloques_llenos
        barra = "[" + "■" * bloques_llenos + "-" * bloques_vacios + "]"
        print(f"{barra} {porcentaje}%", end="\r")
        crear_retraso(100)
    print(f"[{'■' * 20}] 100% ¡Completo!")


def animacion_texto_movil():
    """Anima un texto moviéndose de izquierda a derecha"""
    # TODO: Implementar animación de texto
    # - Definir el texto a animar
    # - Usar un loop para cada posición
    # - En cada iteración, imprimir espacios + texto
    # - Incrementar los espacios para simular movimiento
    # - Limpiar la línea anterior con \r
    textito = str(input("Dame el texto a animar: "))
    for espacios_vacios in range(0, 50):
        print("0" * espacios_vacios + textito, end="\r")
        crear_retraso(70)


def menu_animaciones():
    """Menú para animaciones"""
    print("\n--- ANIMACIONES ---")
    print("1. Barra de Progreso")
    print("2. Texto en Movimiento")
    print("3. Volver al menú principal")
    usuario = str(input("\nElige opcion"))

    # TODO: Implementar lógica del menú

    pass  # Reemplazar con su código

# ============================================
# ALMACENAMIENTO
# ============================================

def actualizar_historial(patron):
    global HISTORIAL
    HISTORIAL.append(patron)
    return HISTORIAL

def cargar_historial():
    global HISTORIAL
    with open(GALERIA_ARCHIVO,mode="r",encoding="utf-8") as f:
        contenido = f.read()
    if contenido == "":
        return
    patrones = contenido.split("=" * 40)
    HISTORIAL = [p.strip("\n") for p in patrones if p.strip()]

def mostrar_historial():
    global HISTORIAL
    print("GALERÍA DE PATRONES:\n")
    for p in HISTORIAL:
        print(p)
        print("-" * 40)


def almacenar_patrones():
    global HISTORIAL
    numero_patron = 1
    if not os.path.isdir(RUTA_DATOS):
        os.mkdir(RUTA_DATOS)
    with open(GALERIA_ARCHIVO,mode="w",encoding="utf-8") as f:
        for pieza in HISTORIAL:
            f.write(f"Patron: {numero_patron}\n")
            f.write(pieza)
            f.write("=" * 40 + "\n")
            numero_patron += 1


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
    print("║           ¡Bienvenido a la Galería de Arte ASCII!          ║")
    print("║                                                            ║")
    print("║    Donde la creatividad se encuentra con la programación   ║")
    print("╚════════════════════════════════════════════════════════════╝")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            print("Mostrando Patrones Geométricos...")
        elif opcion == "2":
            print("Generador de Banner...")
        elif opcion == "3":
            print("Marcos Decorativos...")
        elif opcion == "4":
            print("Animaciones...")
        elif opcion == "5":
            print("Tabla de Multiplicar Visual...")
        elif opcion == "6":
            print("\n" + "="*60)
            print("  ¡Gracias por visitar la Galería de Arte ASCII!")
            print("  Creado con ❤️  y código por: Perla, Miguel, Ariel, Martha")
            print("="*60)
            continuar = False
        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

        if continuar and opcion != "6":
            pausar()
        input("\nPresiona Enter para volver al menú...")
    print("\nPrograma terminado. ¡Hasta pronto! 🎨")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
