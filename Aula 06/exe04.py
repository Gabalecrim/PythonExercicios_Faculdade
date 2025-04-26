def multiplica_por_tres(lista):
    return list(map(lambda x: x * 3, lista))

numeros = [1, 2, 3, 4, 5]
resultado = multiplica_por_tres(numeros)
print(resultado)
