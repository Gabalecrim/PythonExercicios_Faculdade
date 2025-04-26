def filtra_impares(lista):
    return list(filter(lambda x: x % 2 != 0, lista))

numeros = [1, 2, 3, 4, 5, 6, 7]
resultado = filtra_impares(numeros)
print(resultado)
