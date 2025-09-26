import sys
edad = int(input("¿Qué edad tienes?"))
while edad < 0:
    print("Edad no válida.")
    edad = int(input("¿Qué edad tienes?"))
if edad >= 18:
    nivel_fisico = int(input("¿Cuál es tu nivel físico?"))
    while not(1 <= nivel_fisico <= 10):
        print("Nivel físico no válido, tiene que estar entre 1 y 10")
        nivel_fisico = int(input("¿Cuál es tu nivel físico?"))
    if nivel_fisico < 5:
        print("Debes estar en mejor forma, no puedes viajar.")
        sys.exit()
    else:
        print("¡Listo para despegar!")
else:
    print("No puedes viajar.")
    sys.exit()

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