# def crear_retraso(duracion):
#     """
#     Crea un retraso usando un loop vacío.
#
#     Args:
#         duracion (int): Factor de duración (más alto = más lento)
#     """
#     # TODO: Implementar retraso
#     # Usar un loop for que no haga nada
#     for _ in range(duracion * 100000):
#         pass
#
#
# def barra_progreso():
#     """Muestra una barra de progreso animada"""
#     # TODO: Implementar barra de progreso
#     # - Usar un loop de 0 a 100
#     # - En cada iteración, mostrar la barra actualizada
#     # - Usar caracteres como █ ■ o # para la barra llena
#     # - Usar - o espacio para la parte vacía
#     # - Mostrar el porcentaje
#
#     # Ejemplo de salida:
#     # Procesando...
#     # [■■■■■■■■■■----------] 50%
#     # [■■■■■■■■■■■■■■■■----] 80%
#     # [■■■■■■■■■■■■■■■■■■■■] 100% ¡Completo!
#
#     # Pista: usar end="\r" en print para sobrescribir la misma línea
#     print("Procesando...")
#     total_bloques = 20
#     for porcentaje in range(0, 101, 5):
#         bloques_llenos = porcentaje * total_bloques // 100
#         bloques_vacios = total_bloques - bloques_llenos
#         barra = "[" + "■" * bloques_llenos + "-" * bloques_vacios + "]"
#         print(f"{barra} {porcentaje}%", end="\r")
#         crear_retraso(100)
#     print(f"[{'■' * 20}] 100% ¡Completo!")
#
# def animacion_texto_movil():
#     """Anima un texto moviéndose de izquierda a derecha"""
#     # TODO: Implementar animación de texto
#     # - Definir el texto a animar
#     # - Usar un loop para cada posición
#     # - En cada iteración, imprimir espacios + texto
#     # - Incrementar los espacios para simular movimiento
#     # - Limpiar la línea anterior con \r
#     textito = str(input("Dame el texto a animar: "))
#     for espacios_vacios in range(0,50):
#         print("0"*espacios_vacios + textito,end="\r")
#         crear_retraso(70)

import os


HISTORIAL = []
RUTA_BASE = os.path.dirname(__file__)
RUTA_DATOS = os.path.join(RUTA_BASE,"datos")
GALERIA_ARCHIVO = os.path.join(RUTA_BASE,"datos","galeria.txt")

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

cargar_historial()

mostrar_historial()





