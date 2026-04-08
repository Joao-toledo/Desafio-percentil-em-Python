qtd_numeros = int(input("Quantos números você quer na lista? "))

lista = []

for i in range(qtd_numeros):
    valor = int(input(f"Digite o {i+1}º número: "))
    lista.append(valor)
    print("Lista:", lista)

lista.sort()
print("Lista ordenada:", lista)

def calculo_percentil(lista, p):
    n = len(lista)
    posicao = (p / 100) * (n - 1)
    indice_inferior = int(posicao)

    if posicao == indice_inferior:
        return lista[indice_inferior]

    indice_superior = indice_inferior + 1
    valor_inferior = lista[indice_inferior]
    valor_superior = lista[indice_superior]

    valor = valor_inferior + (posicao - indice_inferior) * (valor_superior - valor_inferior)
    return valor

p25 = calculo_percentil(lista, 25)
p50 = calculo_percentil(lista, 50)
p75 = calculo_percentil(lista, 75)

print("\nResultados dos Percentis:")
print(f"P25: {p25}")
print(f"P50 (Mediana): {p50}")
print(f"P75: {p75}")