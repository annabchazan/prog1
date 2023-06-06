"""7. Faça um programa que funciona como uma agenda
telefônica. A agenda deve ser guardada em uma lista com o
seguinte formato: [[‘Ana’, ‘99999-1234’], [‘Bia’, ‘99999- 5678’]]. O programa deve ter um menu que tenha as
seguintes opções:
(a) Adicionar telefones na agenda -- isso deve ser feito de
forma que ela se mantenha sempre ordenada -- cada nome
novo já deve ser inserido na posição correta dentro da
agenda
(b) Procurar um telefone -- o usuário informa um nome e o
programa mostra o número do telefone, ou diz que não
está na agenda
A busca deve ser inteligente: deve parar assim que
encontrar um nome maior do que o nome que está sendo
buscado, ao invés de percorrer a lista sempre até o final
para concluir que um nome não está na agenda."""

agenda = [['Ana', '99999-1234']]

a =  int(input("deseja add um novo contato? 1-sim 0-nao"))
teste = []

 #sem ordem alfabética 
if(a==1):
    teste.append(input('nome'))
    teste.append(input("telefone"))
agenda.append(teste)


b = int(input("deseja procurar algm? 1-sim 0-nao"))
qtt =0 
if(b==1):
   nome = input("nome")
   for i in range(len(agenda)):
    if(agenda[i][0]==nome):
        print(agenda[i][1])
        qtt+=1
        if(qtt == len(agenda)):
            print("não está na agenda")