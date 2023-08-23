"""
faça um programa que preencha por leitura um vetor de 10 posiçoes, e conta quantos valores diferentes existem no vetor
"""
vetor = []

for i in range(10):
    valor = int(input(f"Digite o valor {i + 1}: "))
    vetor.append(valor)

valores_unicos = set(vetor)

quantidade_valores_unicos = len(valores_unicos)

print("Quantidade de valores diferentes no vetor:", quantidade_valores_unicos)
