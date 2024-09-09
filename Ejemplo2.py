def calcular(valor1, valor2, sumando):
    resultado = valor1 * valor2 + sumando
    return resultado

    resultado = calcular(valor1, valor2, sumando)
    print("El resultado es:", resultado)

if __name__ == "__main__":
    valor1 = float(input("Multiplicando:"))
    valor2 = float(input("Multiplicador:"))
    sumando =float(input("Sumando:"))
    resultado = calcular(valor1, valor2, sumando)

    print(f"{valor1}*{valor2}+{sumando}={resultado}")

