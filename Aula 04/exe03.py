def calcular_media(lista):
    if not lista:  # verifica se a lista está vazia
        return 0
    return sum(lista) / len(lista)

valores = [10, 20, 30, 40]
media = calcular_media(valores)
print("Média:", media)
