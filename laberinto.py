laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

camino = [[0 for j in range(9)] for i in range(9)]
filas_mov = [-1, 0, 1, 0]
columnas_mov = [0, 1, 0, -1]

def mostrar_laberinto(matriz):
    for i in range(9):
        for j in range(9):
            print(matriz[i][j], end="\t")
        print()

def valor_celda(celda):
    if celda == 'I' or celda == 'F':
        return 1
    return celda

def buscar_camino(fila, columna, puntos):
    camino[fila][columna] = 1
    if laberinto[fila][columna] == 'F':
        if puntos >= 23:
            return True
        camino[fila][columna] = 0
        return False

    for k in range(4):
        nueva_fila = fila + filas_mov[k]
        nueva_columna = columna + columnas_mov[k]

        if nueva_fila < 0 or nueva_fila >= 9:
            continue
        if nueva_columna < 0 or nueva_columna >= 9:
            continue
        if laberinto[nueva_fila][nueva_columna] == 0:
            continue
        if camino[nueva_fila][nueva_columna] == 1:
            continue
        nuevos_puntos = puntos + valor_celda(
            laberinto[nueva_fila][nueva_columna]
        )

        if buscar_camino(
            nueva_fila,
            nueva_columna,
            nuevos_puntos
        ):
            return True
    camino[fila][columna] = 0
    return False

print("=======================LABERINTO ORIGINAL========================")
mostrar_laberinto(laberinto)
resultado = buscar_camino(8, 0, 1)

if resultado:
    print("\nEl ratón logró salir del laberinto")
    print("El raton obtuvo al menos 23 puntos.")

    print("\nCamino recorrido por el ratón:")
    for i in range(9):
        for j in range(9):
            if laberinto[i][j] == 'I':
                print('I', end="\t")
            elif laberinto[i][j] == 'F':
                print('F', end="\t")
            elif camino[i][j] == 1:
                print('*', end="\t")
            else:
                print(laberinto[i][j], end="\t")
        print()

    puntos_totales = 0

    for i in range(9):
        for j in range(9):
            if camino[i][j] == 1:
                puntos_totales += valor_celda(laberinto[i][j])
    print("\nPuntos obtenidos:", puntos_totales)

else:
    print("\nEl ratón no pudo salir del laberinto")
    print("No se encontro un camino con 23 puntos.")
    print("\nMatriz del camino")
    mostrar_laberinto(camino)
