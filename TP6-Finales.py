
#Ejercicio 10
def cifras(a,b):
    positivo = 0
    error = 0
    contador = 0
    if a < 0:
        a = a * -1
        positivo = positivo + 1
    while contador < b:
        contador = contador + 1
        a = a // 10
    if a < 1:
        a = a * 10
    if a == 0:
        error = error + 1
    if error == 0:
        if positivo == 0:
            print(a%10)
        else:
            print((a%10) * -1)
    else:
        print(-1)

c = int(input("A:"))
v = int(input("B:"))
cifras(c,v)

#Ejercicio 1
def sumaMultiplicacion(a,b):
    total = 0
    while b >= 1:
        total = total + a
        b = b - 1
    return total
valorA = int(input("Ingresa el primer valor: "))
valorB = int(input("Ingresa el segundo valor: "))
print(sumaMultiplicacion(valorA,valorB))

#Ejercicio 2
def numeroElevado(x,y):
    total = 1
    while y >= 1:
        total = sumaMultiplicacion(total,x)
        y = y - 1
    return total

valorC = int(input("Ingresa el primer valor: "))
valorD = int(input("Ingresa el segundo valor: "))


#Ejercicio 3

def asteriscos(a):
    while a < 0:
        a = int(input("Error, dato no valido: "))
    while a > 0:
        print("*")
        a = a - 1
b = int(input("Ingrese un valor: "))
asteriscos(b)

#Ejercicio 5
def signo(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0
n = int(input("Ingrese un numero entero: "))
print(signo(n))

#Ejercicio 11
def digitosContar(b):
    numero2 = b
    contador = 0
    while b > 0:
        b = b // 10
        contador = contador + 1
    contador2 = contador
    if contador % 2 == 0:
        return -1
    else:
        while contador > (contador2 // 2 + 1):
            numero2 = numero2 // 10
            contador = contador - 1
        return numero2 % 10

numero = int(input("Ingrese un numero: "))
print(digitosContar(numero))

#Ejercicio 4
def multiplo(a,b):
    if a % b == 0:
        return True
    else:
        return False
xy = int(input("Ingrese valor 1: "))
xyz = int(input("Ingrese valor 2: "))

print(multiplo(xy,xyz))





