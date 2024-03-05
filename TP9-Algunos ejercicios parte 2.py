#Ejercicio 3

import random

def ordenamiento(v):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(v)-1):
            if v[i]>v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                desordenado = True
    return v

#PRINTS EN PANTALLA
print("Vamos a jugar un juego...")
print("Tenemos un numero generado al azar, de cuatro cifras, lo que tenes que hacer es adivinar el numero y nosotros")
print("te vamos a ir dando pistas de si el numero es mayor o menor.")

#VARIABLES
contador = 0
record = 5
empezardecero = 1
dniMejores = []
contadorMejores = []

#INPUTS
numero = int(input("Ingrese el numero para empezar a adivinar: "))
adivinar = random.randint(10,90)

#CONDICIONALES
while numero != -1 and empezardecero == 1:
    if numero < adivinar:
        print("El numero es mayor...")
        contador = contador + 1
    elif numero > adivinar:
        print("El numero es menor...")
        contador = contador + 1
    else:
        print("Felicidades!!!, el numera era",adivinar)
        print("La cantidad de intentos fue de:",contador)
        if contador <= record:
            record = contador
            dni = int(input("Establecio un nuevo record! Introduzca su DNI para guardarlo: "))
        empezardecero = int(input("Si desea volver a empezar coloque 1, en caso contrario coloque 0: "))
        if empezardecero == 1:
            adivinar = random.randint(10,90)
        else:
            numero = -1
        contadorMejores.append(contador)
        contador = 0
        while len(contadorMejores) > 5:
            del contadorMejores[5]
    if numero != - 1:
        numero = int(input("Vuelve a adivinar el numero ")) 

print("Las mejores puntuaciones fueron las siguientes 5:",ordenamiento(contadorMejores))



