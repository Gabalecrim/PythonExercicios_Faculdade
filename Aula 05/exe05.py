nota = float(input("Digite a nota do aluno: "))

if 9 <= nota <= 10:
    print("Classificação: A")
elif 7 <= nota < 9:
    print("Classificação: B")
elif 5 <= nota < 7:
    print("Classificação: C")
elif 0 <= nota < 5:
    print("Classificação: D")
else:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
