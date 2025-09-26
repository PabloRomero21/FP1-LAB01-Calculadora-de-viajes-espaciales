distancia = int(input("Introduce la distancia total en km:"))
distancia_recorrida= 0
parada = 0
while distancia_recorrida < distancia-15000:
    distancia_recorrida = distancia_recorrida + 15000
    parada= parada+1
    print(f"Parada en el km {distancia_recorrida}")
print(f"Total de paradas para respostar: {parada}")