"""6. Faça um programa que manipula uma lista que contém modelos de
carro e seu consumo (km/l), da seguinte forma: [[‘Vectra’, 9], [‘Gol’, 10],
[‘Corsa’, 11], [‘Fit’, 12.5]]. O programa deve mostrar na tela o nome do
modelo mais econômico. Além disso, deve mostrar na tela quanto cada
um desses modelos gastaria para percorrer 1000 Km, assumindo que o
valor do litro da gasolina é R$ 3,50."""

carros = [['Vectra', 9], ['Gol', 10] ,['Corsa', 11] ,['Fit', 12.5]]

print(carros)
eco = carros[0][1]
carro_eco = 0 
preco = 0


for i in range (4):
    preco = (1000*3.5)/carros [i][1]
    print(f'{carros[i][0]} gasta ->{round(preco,2)}')
    if( carros [i][1]<eco):
        eco = carros [i][1]
        carro_eco = i
       

print(carros[carro_eco][0])