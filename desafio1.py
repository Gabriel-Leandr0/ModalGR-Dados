def buscar_repetidos(a, b):
    repetidos = []

    for num in a:
        if num in b and num not in repetidos:
            repetidos.append(num)

    return repetidos


vetor_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor_b = [4, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

vetor_final = buscar_repetidos(vetor_a, vetor_b)
print(vetor_final)
