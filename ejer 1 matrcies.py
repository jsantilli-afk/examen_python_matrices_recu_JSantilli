matriz = []
def cargar_matriz():
    global matriz
    filas = int(input("filas: "))
    columnas = int(input("columnas: "))
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
def mostrar_matriz():
    for i in range(len(matriz)):
        fila_texto = ""
        for j in range(len(matriz[i])):
            fila_texto = fila_texto + str(matriz[i][j]) + " "
        print(fila_texto)
def sumatoria():
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma = suma + matriz[i][j]
    print("suma:", suma)
def productoria():
    producto = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            producto = producto * matriz[i][j]
    print("El producto de todos los elementos es", producto)
def transpuesta():
    filas = len(matriz)
    columnas = len(matriz[0])
    for j in range(columnas):
        fila_texto = ""
        for i in range(filas):
            fila_texto = fila_texto + str(matriz[i][j]) + " "
        print(fila_texto)
opcion = -1
while opcion != 0:
    print("1. Cargar")
    print("2. Mostrar")
    print("3. Sumar")
    print("4. Productoria")
    print("5. Transpuesta")
    print("0. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        cargar_matriz()
    elif opcion == 2:
        mostrar_matriz()
    elif opcion == 3:
        sumatoria()
    elif opcion == 4:
        productoria()