"""Faça um programa que leia uma matriz 3x3 e
multiplique os elementos da diagonal principal da matriz
por um número k. Imprima a matriz na tela antes e
depois da multiplicação."""

k = int(input("num"))
matriz = []


for i in range(3):
    linha = []
    for y in range(3):
        linha.append(int(input("valor")))
    matriz.append(linha)

matriz_mult = matriz

for z in range(3):
    (matriz_mult[z][z])=(matriz[z][z])*k


for w in range(3):
    print(matriz[w])
 

print()

for y in range(3):
    print(matriz_mult[y])