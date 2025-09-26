distancia = int(input("Introduce la distancia total en km:"))
distancia_recorrida= 0
parada = 0
while distancia_recorrida <= distancia:
    distancia_recorrida = distancia_recorrida + 150000
    parada= parada+1
    print(f"Parada en el km {disatncia_recorrida}")
print(f"Total de paradas para respostar: {parada}")