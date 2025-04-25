def imprimir_lista_numerada(lista):
    for i, elemento in enumerate(lista, start=1):
        print(f"{i}. {elemento}")
        
minha_lista = ["maçã", 42, True, 3.14, "Gabriel"]
imprimir_lista_numerada(minha_lista)

