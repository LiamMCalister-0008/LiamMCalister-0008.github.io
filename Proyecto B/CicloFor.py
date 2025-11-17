import random

for  i  in range(5):
    print("Bienvenido")
    Vidas = random.randint(1,5)
    print("Tenes", Vidas, "Vidas")

    if Vidas>=5:
        print("Estas en Dificultad FACIL")
    else:
        if Vidas>3:
            print("Estas en Dificultad MEDIA")
        if Vidas>1:
            print("Estas en Dificultad DIFICIL")
print("Fin del Juego")