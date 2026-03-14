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
    print("     Creado por: [El Ecuipo alfa dinamita omega masísa]")
    print("     Creado por: Perla, Miguel, Ariel, Martha")
    print("="*60)
    print("\nGALERÍA:")
    print("1. Patrones Geométricos")
    print("2. Generador de texto artisticos")
    print("3. Animaciones")
    print("4. Mostrar galeria")
    print("5. Salir")
    print("-"*60)


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

def menu_patrones():
    """
    Muestra un menú interactivo para generar patrones geométricos.

    Permite al usuario seleccionar entre diferentes figuras ASCII
    (triángulo, cuadrado o pirámide), solicitar el tamaño del patrón
    y mostrar el resultado en pantalla. Cada patrón generado se
    almacena en el historial de la galería.

    El menú continúa ejecutándose hasta que el usuario decide
    volver al menú principal.
    """
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
                    patron = triangulo(altura=tamano)
                    print(patron)
                    actualizar_historial(patron=patron)
                elif opcion == "2":
                    patron = cuadrado(lado=tamano)
                    print(patron)
                    actualizar_historial(patron=patron)
                elif opcion == "3":
                    patron = piramide(altura=tamano)
                    print(patron)
                    actualizar_historial(patron=patron)
                # Preguntar si desea ver otro patrón
                continuar = input("\n¿Desea ver otro patrón? (s/n): ").lower()
                if continuar != 's':
                    break
                    
            except ValueError:
                print("Error: Por favor, ingrese un número entero para el tamaño.")
        else:
            print("Opción no válida. Intente de nuevo.")



# ============================================
# SECCIÓN 3: TEXTO ARTÍSTICO (Estudiante 2)
# ============================================

def generar_banner(texto):
    """
    Genera un banner decorativo con el texto proporcionado.

    El texto se muestra en mayúsculas dentro de un marco ASCII
    utilizando caracteres decorativos. El banner se imprime en
    pantalla y también se devuelve como cadena para poder ser
    guardado en el historial.

    Args:
        texto (str): Texto que aparecerá dentro del banner.

    Returns:
        str: Banner generado en formato ASCII.
    """
    linea = "═" * (len(texto) + 4)

    banner = (
        f"╔{linea}╗\n"
        f"║  {texto.upper()}  ║\n"
        f"╚{linea}╝\n"
    )

    print(banner)
    return banner


def marco_decorativo(texto, estilo):
    """
    Genera un marco decorativo alrededor de un texto.

    Dependiendo del estilo seleccionado, el texto se muestra
    dentro de diferentes tipos de bordes ASCII.

    Args:
        texto (str): Texto que se desea enmarcar.
        estilo (int): Estilo del marco.
            1 = Marco elegante con líneas.
            2 = Marco decorativo con estrellas.

    Returns:
        str: Texto enmarcado en formato ASCII.
    """
    largo = len(texto)

    if estilo == 1:
        marco = (
            f"╔{'═' * (largo + 4)}╗\n"
            f"║  {texto}  ║\n"
            f"╚{'═' * (largo + 4)}╝\n"
        )

    elif estilo == 2:
        borde = "★ ☆ " * ((largo // 4) + 2)
        marco = (
            f"{borde}\n"
            f"☆  {texto}  ★\n"
            f"{borde}\n"
        )
    else:
        marco = "Estilo no reconocido."

    print(marco)
    return marco


def tabla_multiplicar_visual(numero):
    """Genera una tabla de multiplicar con formato visual atractivo."""

    titulo = f"TABLA DEL {numero}"
    ancho_interno = 20

    tabla = ""

    # 1. Crear encabezado decorativo
    tabla += f"\n╔{'═' * (ancho_interno + 2)}╗\n"
    tabla += f"║{titulo.center(ancho_interno + 2)}║\n"
    tabla += f"╠{'═' * (ancho_interno + 2)}╣\n"

    # 2. Generar tabla del 1 al 10
    for i in range(1, 11):
        resultado = numero * i
        linea = f"{numero} x {i:>2} = {resultado:>3}"
        tabla += f"║  {linea.center(ancho_interno)}  ║\n"

    # 3. Cerrar con pie decorativo
    tabla += f"╚{'═' * (ancho_interno + 2)}╝\n"

    print(tabla)
    return tabla


def menu_texto_artistico():
    """
    Muestra un menú para generar diferentes estilos de texto artístico.

    El usuario puede crear banners, marcos decorativos o tablas de
    multiplicar visuales. Cada resultado generado se muestra en
    pantalla y se almacena en el historial de la galería.

    El menú permanece activo hasta que el usuario decide regresar
    al menú principal.
    """
    while True:
        print("\n--- GENERADORES DE TEXTO ---")
        print("1. Crear Banner")
        print("2. Marco Decorativo")
        print("3. Tabla de Multiplicar")
        print("4. Volver al menú principal/Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            txt = input("Ingrese el texto para su banner: ")
            patron = generar_banner(txt)
            print(patron)
            actualizar_historial(patron=patron)
            
        elif opcion == "2":
            txt = input("Ingrese el texto a enmarcar: ")
            print("Estilos: 1 (Elegante ═), 2 (Estrellas ★)")
            est = int(input("Elija estilo: "))
            patron = marco_decorativo(txt, est)
            print(patron)
            actualizar_historial(patron=patron)
            
        elif opcion == "3":
            try:
                num = int(input("¿De qué número desea la tabla? (1-10): "))
                patron = tabla_multiplicar_visual(num)
                print(patron)
                actualizar_historial(patron=patron)
            except ValueError:
                print("Por favor, ingrese un número válido.")
                
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")


# ============================================
# SECCIÓN 4: ANIMACIONES (Estudiante 3)
# ============================================

def crear_retraso(duracion):
    """
    Crea un retraso usando un loop vacío.

    Args:
        duracion (int): Factor de duración (más alto = más lento)
    """
    for _ in range(duracion * 100000):
        pass


def barra_progreso():
    """Muestra una barra de progreso animada"""
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
    """
    Crea una animación de texto moviéndose horizontalmente.

    El usuario introduce el texto que desea animar y la distancia
    de movimiento. El programa imprime el texto desplazándose hacia
    la derecha mediante la impresión de espacios progresivos y el
    uso de retorno de carro para actualizar la misma línea.

    Returns:
    None
    """
    textito = str(input("Dame el texto a animar: "))
    verificador = True
    while verificador:
        try:
            movimiento = int(input("¿Cuanto tiene que moverse? "))
            verificador = False
        except ValueError:
            print("Valores no validos")

    for espacios_vacios in range(0, movimiento + 1):
        print(" " * espacios_vacios + textito, end="\r")
        crear_retraso(70)


def menu_animaciones():
    """
    Muestra un menú interactivo para ejecutar animaciones ASCII.

    Permite seleccionar entre diferentes animaciones disponibles,
    como una barra de progreso o texto en movimiento. El usuario
    puede ejecutar animaciones repetidamente hasta decidir regresar
    al menú principal.
    """
    while True:
        """Menú para animaciones"""
        print("\n--- ANIMACIONES ---")
        print("1. Barra de Progreso")
        print("2. Texto en Movimiento")
        print("3. Volver al menú principal")
        usuario = str(input("\nElige opcion"))
        if usuario == "1":
            print("Generando barra de progreso")
            barra_progreso()
        elif usuario == "2":
            print("Generando animación")
            animacion_texto_movil()
        elif usuario == "3":
            return
        else:
            print("Esa opcion no se encuentra disponible")

# ============================================
# ALMACENAMIENTO
# ============================================

def actualizar_historial(patron):
    """
    Agrega un nuevo patrón ASCII al historial de la galería.

    Args:
        patron (str): Representación del arte ASCII generado.

    Returns:
        list: Lista actualizada del historial de patrones.
    """
    global HISTORIAL
    HISTORIAL.append(patron)
    return HISTORIAL

def cargar_historial():
    """
    Muestra todos los patrones almacenados en la galería.

    Recorre la lista HISTORIAL e imprime cada patrón ASCII
    en pantalla separado por líneas divisorias para facilitar
    su lectura.

    Returns:
        None
    """
    global HISTORIAL
    if not os.path.exists(GALERIA_ARCHIVO):
        return
    with open(GALERIA_ARCHIVO,mode="r",encoding="utf-8") as f:
        contenido = f.read()
        if contenido == "":
            return
    patrones = contenido.split("=" * 40)

    limpio = []

    for p in patrones:
        lineas = p.strip().split("\n")

        # eliminar la línea "Patron: n"
        if lineas and lineas[0].startswith("Patron"):
            lineas = lineas[1:]

        limpio.append("\n".join(lineas))

    HISTORIAL = [p for p in limpio if p.strip()]



def mostrar_historial():
    """
    Muestra todos los patrones almacenados en la galería.

    Recorre la lista HISTORIAL e imprime cada patrón ASCII
    en pantalla separado por líneas divisorias para facilitar
    su lectura.

    Returns:
        None
    """
    global HISTORIAL
    print("GALERÍA DE PATRONES:\n")
    if HISTORIAL == []:
        print("No existe")
        return
    for p in HISTORIAL:
        print(p)
        print("-" * 40)


def almacenar_patrones():
    """
    Guarda todos los patrones del historial en un archivo.

    Cada patrón se escribe en el archivo de galería con una
    numeración consecutiva y un separador visual para facilitar
    su lectura cuando se cargue posteriormente.

    Returns:
        None
    """
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
    """
    Simula la limpieza de la pantalla en la consola.

    Imprime múltiples saltos de línea para desplazar el
    contenido anterior fuera del área visible de la terminal.

    Returns:
        None
    """
    # No usamos os.system() porque no está en los módulos 1-6
    print("\n" * 50)


def pausar():
    """
    Detiene temporalmente la ejecución del programa.

    Espera a que el usuario presione la tecla Enter antes
    de continuar, permitiendo que el usuario lea la salida
    mostrada en pantalla.

    Returns:
    None
    """
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
    cargar_historial()

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            print("Mostrando Patrones Geométricos...")
            menu_patrones()
        elif opcion == "2":
            print("Generador de texto artistico y tabla de multiplicar...")
            menu_texto_artistico()
        elif opcion == "3":
            print("Animaciones...")
            menu_animaciones()
        elif opcion == "4":
            print("Galeria...")
            mostrar_historial()
        elif opcion == "5":
            almacenar_patrones()
            print("\n" + "="*60)
            print("  ¡Gracias por visitar la Galería de Arte ASCII!")
            print("  Creado con ❤️  y código por: Perla, Miguel, Ariel, Martha")
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
