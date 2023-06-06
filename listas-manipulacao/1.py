"""1. Faça um programa que percorre uma lista com o seguinte formato:
[['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha',
[7,8]]]. Essa lista indica o número de faltas que cada time fez em cada
jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a
Itália fez 9. O programa deve imprimir na tela:
(a) o total de faltas do campeonato
(b) o time que fez mais faltas
(c) o time que fez menos faltas"""

jogos = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha',
[7,8]]]

total_faltas = 0
pais_faltas = []
maior = 0
maior_id = 0
menor = jogos[0][2][0] + jogos[1][2][0]
menor_id = 0

for i in range(3):
    for j in range(2):
        total_faltas+=(jogos[i][2][j])

pais_faltas.append(jogos[0][2][0] + jogos[1][2][0])
pais_faltas.append(jogos[0][2][1] + jogos[2][2][0])
pais_faltas.append(jogos[1][2][1] + jogos[2][2][1])

print(pais_faltas)

for k in range (3):
    if(pais_faltas[k] >= (maior)):
        maior=pais_faltas
        maior_id = k

for w in range (3):
    if(pais_faltas[w]<=menor):
        manor = pais_faltas[w]
        menor_id=w

if(k == 0):
    print('brasil mais faltas')
elif(k==1):
    print('it mais faltas')
else:
    print('espanha mais faltas')



if(w == 0):
    print('brasil menos faltas')
elif(w==1):
    print('it menos faltas')
else:
    print('espanha menos faltas')



print("faltas:", total_faltas)

