def is_mutant(dna):
    rows = len(dna) #numero de filas en la matriz
    cols = len(dna[0])  #numero de columnas en la matriz


    # funcion auxiliar para verificar si hay una secuencia de cuatro letras iguales en una direccion especifica
    def check_sequence(x, y, dx, dy, leter): # "x" e "y" : coordenadas iniciales de la matriz // "dx" y "dy":especifican la direccion // leter:letra que buscamos
        for i in range(4):  #uso el bucle FOR para verificar si hay cuatro letras iguales en la dirección especificada
            if x < 0 or x >= rows or y < 0 or y >= cols or dna[x][y] != leter:
                return False #si no se encuentra una secuencia completa
            x += dx
            y += dy
        return True #si se encuentra la secuencia completa
    
    # verificar horizontalmente
    for i in range(rows):
        for j in range(cols - 3): # itera sobre las columnas (hasta la tercera columna antes del final) (igual en todos los bucles)
            if check_sequence(i, j, 0, 1, dna[i][j]): #invocamos la funcion auxiliar pasando los respectivos parametros (igual en todos los bucles)
                return True

    # verificar verticalmente
    for i in range(rows - 3):
        for j in range(cols):
            if check_sequence(i, j, 1, 0, dna[i][j]):
                return True

    # verificar diagonalmente (derecha y abajo)
    for i in range(rows - 3):
        for j in range(cols - 3):
            if check_sequence(i, j, 1, 1, dna[i][j]):
                return True

    # verificar diagonalmente (izquierda y abajo)
    for i in range(rows - 3):
        for j in range(3, cols):
            if check_sequence(i, j, 1, -1, dna[i][j]):
                return True

    return False # si en ninguna secuencia encontramos 4 letras iguales la funcion devuelte FALSE
