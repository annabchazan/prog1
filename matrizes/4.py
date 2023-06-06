"""Faça um programa que leia uma matriz 3x3 de inteiros e
retorne a linha de maior soma. Imprima na tela a matriz, a
linha de maior soma e a soma."""

matriz = []
soma = [0,0,0]
maior = 0
maior_id = 0

for i in range(3):
    linha = []
    for j in range(3):
        l=int(input("valor"))
        soma[i]+=l
        linha.append(l)
    matriz.append(linha)

for i in range(3):
    if soma [i] >maior:
        maior = soma[i]
        maior_id = i

print(matriz[maior_id])
print(soma[maior_id])



