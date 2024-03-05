import random

n = int(input("Ingrese un valor entre el 1 y el 20: "))
secuencias = []
suma = 0
j = 0
for i in range(0,n):
    secuencias.append(random.randint(1,20))
    
while suma < 20:
    suma = secuencias[j] + secuencias[j+1] + suma
    j = j+1
print(secuencias)
print(suma)