lista = [10, 13, 15, 19, 23, 24, 27, 31, 33, 35, 37]
lista.sort()

def calculo_percentil(lista, p):
    n = len(lista)

    posicao = (p / 100) * (n - 1)

    indice_inferior = int(posicao)

    # Se for inteira. Ex: mediana
    if posicao == indice_inferior:
        return lista[indice_inferior]

    indice_superior = indice_inferior + 1

    valor_inferior = lista[indice_inferior]
    valor_superior = lista[indice_superior]

    valor = (valor_inferior + valor_superior) / 2

    return valor


p25 = calculo_percentil(lista, 25)
p50 = calculo_percentil(lista, 50)
p75 = calculo_percentil(lista, 75)

print(" Resultados dos Percentis:")
print(f"P25: {p25}")
print(f"P50 (Mediana): {p50}")
print(f"P75: {p75}")