def crear_retraso(duracion):
    """
    Crea un retraso usando un loop vacío.

    Args:
        duracion (int): Factor de duración (más alto = más lento)
    """
    # TODO: Implementar retraso
    # Usar un loop for que no haga nada
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
    for espacios_vacios in range(0,50):
        print("0"*espacios_vacios + textito,end="\r")
        crear_retraso(70)

barra_progreso()
animacion_texto_movil()