"""
dada a lista [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52] faça um programa que:
imprima o maior elemento 
imprima o menor elemento 
imprima os numreos pares 
imprima o numero de ocorrencias do primeiro elemento na lista
imprima a media dos elementos  
imprima a soma dos valores negativos
"""
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# a) Maior elemento
maior_elemento = max(lista)
print("Maior elemento:", maior_elemento)

# b) Menor elemento
menor_elemento = min(lista)
print("Menor elemento:", menor_elemento)

# c) Números pares
numeros_pares = [num for num in lista if num % 2 == 0]
print("Números pares:", numeros_pares)

# d) Número de ocorrências do primeiro elemento
primeiro_elemento = lista[0]
ocorrencias_primeiro_elemento = lista.count(primeiro_elemento)
print("Número de ocorrências do primeiro elemento:", ocorrencias_primeiro_elemento)

# e) Média dos elementos
media_elementos = sum(lista) / len(lista)
print("Média dos elementos:", media_elementos)

# f) Soma dos elementos de valor negativo
soma_negativos = sum([num for num in lista if num < 0])
print("Soma dos elementos de valor negativo:", soma_negativos)
