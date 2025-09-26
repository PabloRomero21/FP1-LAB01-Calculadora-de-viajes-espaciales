distancia_km = int(input("¿Cuanta distancia vas a recorrer en kilometros?"))
velocidad_kmh = int(input("¿A qué velocidad vas a viajar (km/h)?"))
tiempo_minutos = (distancia_km / velocidad_kmh) * 60
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
if tiempo_horas < 1:
    print(f"Tardarías {tiempo_minutos} minutos en llegar.")
elif tiempo_dias < 1:
    print(f"Tardarías {tiempo_horas} horas en llegar.")
else:
    print(f"Tardarías {tiempo_dias} días en llegar.")