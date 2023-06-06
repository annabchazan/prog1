"""4. Faça um programa que percorre duas listas e intercala os elementos
de ambas, formando uma terceira lista. A terceira lista deve começar
pelo primeiro elemento da lista menor.

Exemplo:
lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]
lista_intercalada = [1, 10, 2, 20, 3, 30, 4, 40, 50, 60]"""

lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]
lista_intercalada = []

for i in range(4):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])


for j in range(4, 6):
    lista_intercalada.append(lista2[j])

print(lista_intercalada)