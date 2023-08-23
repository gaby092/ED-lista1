"""
faça um programa que preencha por leitura um vetor de 5 posiçoes, informe a posiçao em que um valor x aparece pela primeira vez no vetor. 
caso o valor x nao seja encontrado, o programa deve imprimir o valor -1
"""
vetor = []

for i in range(5):
    valor = int(input(f"Digite o valor {i + 1}: "))
    vetor.append(valor)

x = int(input("Digite o valor que deseja encontrar: "))

posicao = -1

for i in range(len(vetor)):
    if vetor[i] == x:
        posicao = i  
        break 

print("Posição onde o valor x aparece pela primeira vez:", posicao)
