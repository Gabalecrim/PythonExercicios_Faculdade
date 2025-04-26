frutas = ["abacaxi", "banana", "amora", "laranja", "acerola", "uva"]

def frutas_com_a(lista):
    return [fruta for fruta in lista if fruta.lower().startswith('a')]

frutas_a = frutas_com_a(frutas)
print(frutas_a)
