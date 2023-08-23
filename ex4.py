"""
um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor.faça um programa que simule o lançamento do dado
 e determine o porcentual de ocorrencias de face 6 do dado dentre esses 50 lançamentos.
"""
import random

ocorrencias_face_6 = 0

for _ in range(50):
    resultado = random.randint(1, 6)  
    if resultado == 6:
        ocorrencias_face_6 += 1  

percentual_face_6 = (ocorrencias_face_6 / 50) * 100

print(f"Percentual de ocorrências da face 6: {percentual_face_6}%")
