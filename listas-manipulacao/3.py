"""3. Faça um programa que percorre um vetor e imprime na tela o valor
mais próximo da média dos valores do vetor. Exemplo:

vetor = [2.5, 7.5, 10.0, 4.0]
(média = 6.0)
Valor mais próximo da média = 7.5"""

vetor = [2.5, 7.5, 10.0 , 4.0]
soma = 0
tam = len(vetor)


for i in range(tam):
    soma += vetor[i]

media = soma/tam

menor_diferença = abs(vetor[0] - media)
menor = 0

for y in range(tam):
    if(abs(vetor[y] - media) < menor_diferença):
        menor_diferença = abs(vetor[y] - media)
        menor = y

print(vetor[menor])
print(media)

'''abs -> módulo'''