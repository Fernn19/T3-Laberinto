N = 9
PUNTAJE_MINIMO = 23

laberinto = [
    ["F", 1, 1, 3, 0, 1, 1, 1, 4],
    [3,   0, 0, 1, 0, 1, 0, 0, 1],
    [1,   1, 0, 1, 1, 1, 1, 0, 1],
    [0,   1, 0, 1, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 1, 1, 3, 1, 1],
    [3,   0, 1, 0, 0, 0, 1, 0, 1],
    [1,   1, 1, 1, 3, 1, 1, 1, 1],
    [1,   0, 0, 1, 0, 1, 0, 0, 4],
    ["I", 1, 3, 1, 0, 1, 1, 1, 1]
]

mov_fila = [-1, 0, 1, 0]
mov_col = [0, 1, 0, -1]

def crear_matriz(valor):
    matriz = []
    for i in range(N):
        fila = []
        for j in range(N):
            fila.append(valor)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for i in range(N):
        linea = ""
        for j in range(N):
            linea = linea + str(matriz[i][j]).rjust(3)
        print(linea)
    print()

def valor_celda(fila, col):
    if laberinto[fila][col] == "I" or laberinto[fila][col] == "F":
        return 1
    return laberinto[fila][col]

def es_valida(fila, col, solucion):
    if fila < 0 or fila >= N or col < 0 or col >= N:
        return False
    if valor_celda(fila, col) == 0:
        return False
    if solucion[fila][col] == 1:
        return False
    return True

def backtracking(fila, col, puntos, solucion):
    solucion[fila][col] = 1
    if valor_celda(fila, col) == 3 or valor_celda(fila, col) == 4:
        puntos = puntos + valor_celda(fila, col)

    if fila == 0 and col == 0:
        if puntos >= PUNTAJE_MINIMO:
            return puntos
        solucion[fila][col] = 0
        return 0
        
    for k in range(4):
        nueva_fila = fila + mov_fila[k]
        nueva_col = col + mov_col[k]
        if es_valida(nueva_fila, nueva_col, solucion):
            resultado = backtracking(nueva_fila, nueva_col, puntos, solucion)
            if resultado > 0:
                return resultado

    solucion[fila][col] = 0
    return 0

def main():
    print("LABERINTO ORIGINAL:")
    imprimir_matriz(laberinto)

    solucion = crear_matriz(0)
    puntos = backtracking(N - 1, 0, 0, solucion)

    if puntos > 0:
        print("EL RATON LOGRO SALIR DEL LABERINTO")
        print("Puntos obtenidos:", puntos)
        print()
        print("MATRIZ SOLUCION (camino a seguir):")
        imprimir_matriz(solucion)
    else:
        print("EL RATON NO LOGRO SALIR: no hay camino con", PUNTAJE_MINIMO, "puntos o mas")
        print()
        print("MATRIZ SOLUCION:")
        imprimir_matriz(solucion)
main()
