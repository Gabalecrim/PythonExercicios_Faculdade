def divisao(quociente, divisor):
    q = quociente // divisor  
    r = quociente % divisor   
    return q, r

resultado = divisao(17, 5)
print(f"Quociente: {resultado[0]}, Resto: {resultado[1]}")
