import random
puntos=0
bandera=True
while bandera :
    print("Usted esta jugando")
    print("Tienes", puntos)
    dado=random.randint(1,6)
    dado2=random.randint(1,6)
    puntos=dado+dado2
    if puntos==12 :
        bandera=False
        print("Ganaste", puntos)