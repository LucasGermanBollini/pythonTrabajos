
#Ejercicio 5
numero = int(input("Ingrese su numero: "))
nespacios = 1
while nespacios <= numero:
    print(nespacios)
    nespacios = nespacios + 1

#Ejercicio 4
impares = 42
total = 0
while impares < 176:
    if impares % 2 == 0:
        impares = impares + 1
    else:
        total = impares + total
print(total)

#Ejercicio 2

impar = 0
nro = int(input("Ingrese un numero y cuando termine introduzca -1: "))
while nro != -1:
    if impar == 0:
        impar = 1
    else:
        impar = 0
    nro = int(input("Ingrese un numero y cuando termine introduzca -1: "))
    
if impar == 1:
    print("La cantidad es impar")
else:
     print("La cantidad es par")

#Ejercicio Clase
 
 
def verificar(a):
    if a >= 0 and a <= 1000:
        total = 1
    else:
        total = 0
    return total       
        
n = float(input("Ingrese un valor entre el 0 y el 1000: "))
if verificar(n) == 1:
    print("El valor ingresado es correcto")
else:
    print("El valor ingresado es incorrecto")
    
def calculo(a):
    if a >= min and a <= max:
        total1 = 1
    else:
        total1 = 0
    return total1
    
    
min = int(input("Ingrese un valor minimo: "))
max = int(input("Ingrese un valor maximo: "))
numero = int(input("Ingrese su numero: "))
if calculo(numero) == 1:
    print("El valor ingresado es correcto")
else:
    print("El valor ingresado no es correcto")
