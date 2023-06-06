"""2. Faça um programa que simule um lançamento de dados. Lance o
dado 10 vezes e armazene os resultados em um vetor. Depois, monte
um outro vetor contendo quantas vezes cada valor foi obtido. Imprima
os dois vetores. Use uma função para gerar números aleatórios,
simulando os lançamentos dos dados.

Exemplo de uma possível saída:
[3, 1, 5, 3, 5, 4, 5, 5, 3, 6]
[1, 0, 3, 1, 4, 1]"""



import random 
r_dado = []
qtt = []
soma = [0,0,0,0,0,0]

for i in range(10):
    r_dado.append(random.randint(1,6))

for y in range(10):
    for z in range(1,7):
        if r_dado[y]==z:
            soma[z-1]+=1
print(r_dado)
print(soma)