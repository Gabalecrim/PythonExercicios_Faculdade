import operator

numero = int(input("Digite um número: "))

resto = operator.mod(numero, 2)

if resto == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
