"""Faça um programa que leia duas matrizes A e B 2x2 e
imprima a matriz C que é a soma das matrizes A e B."""

a = []
b = []
c = []


for i in range(2):
    l_a = []
    for j in range(2):
        l_a.append(int(input("a")))
    a.append(l_a)

for i in range(2):
    l_b = []
    for j in range(2):
        l_b.append(int(input("b")))
    b.append(l_b)


for i in range(2):
    l_c = []
    for j in range(2):
        l_c.append(a[i][j]+b[i][j])
    c.append(l_c)


for w in range(2):
    print(a[w])

print()

for w in range(2):
    print(b[w])

print()

for w in range(2):
    print(c[w])


