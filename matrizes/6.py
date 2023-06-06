'''Uma pista de Kart permite 10 voltas para cada um de 6
corredores. Faça um programa que leia os nomes e os
tempos (em segundos) de cada volta de cada corredor e
guarde as informações em uma matriz. Ao final, o programa
deve informar:
a. De quem foi a melhor volta da prova, e em que volta
b. Classificação final em ordem (1o. o campeão)
c. Qual foi a volta com a média mais rápida'''

corredores = []

for i in range(2):
    tempo = []
    for j in range(4):
        tempo.append(input("nome"))
        tempo.append(int(input("tempo")))
    corredores.append(tempo)

for i in range(2):
    print(corredores[i])