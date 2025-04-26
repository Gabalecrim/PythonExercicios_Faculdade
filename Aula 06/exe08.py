def frutas_guardadas(lista):
    frutas_filtradas = filter(lambda fruta: len(fruta) > 5, lista)
    frutas_mapeadas = map(lambda fruta: f"Fruta guardada: {fruta}", frutas_filtradas)
    return list(frutas_mapeadas)

frutas = ["maçã", "banana", "kiwi", "abacaxi", "uva", "laranja"]
resultado = frutas_guardadas(frutas)
print(resultado)
