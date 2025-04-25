def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = int(input("Digite um número: "))
resultado = eh_par(numero)
print(f"O número {numero} é par? {resultado}")
