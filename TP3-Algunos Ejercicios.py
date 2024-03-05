"""#Ejercicio 1
n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))
if n1 == n2:
    print("Los numeros son iguales.")
else:
    print("Los numeros son distintos.")
    
#Ejercicio 2
numero = int(input("Ingrese un numero entero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

#Ejercicio 3

mes = int(input("Ingrese un numero del 1 al 12: "))
if mes == 1:
    print("El numero corresponde al mes de enero.")
elif mes == 2: 
    print("El numero corresponde al mes de febrero.")
elif mes == 3:
    print("El numero corresponde al mes de marzo.")
elif mes == 4:
    print("El numero corresponde al mes de abril.")
elif mes == 5:
    print("El numero corresponde al mes de mayo.")
elif mes == 6:
    print("El numero corresponde al mes de junio.")
elif mes == 7:
    print("El numero corresponde al mes de julio.")
elif mes == 8:
    print("El numero corresponde al mes de agosto.")
elif mes == 9:
    print("El numero corresponde al mes de septiembre.")
elif mes == 10:
    print("El numero corresponde al mes de octubre.")
elif mes == 11:
    print("El numero corresponde al mes de noviembre.")
elif mes == 12:
    print("El numero corresponde al mes de diciembre.")
else:
    print("Error, valor no valido.")
    
#Ejercicio 4

parcial1 = int(input("Ingrese la nota del primer parcial: "))
parcial2 = int(input("Ingrese la nota del segundo parcal: "))
promedioParcial = (parcial1+parcial2) / 2

if promedioParcial < 4:
    print("El alumno recursa la materia.")
elif promedioParcial < 7:
    print("El alumno va a final.")
else:
    print("El alumno promociona la materia.")

#Ejercicio 5

paginas = int(input("Ingrese la cantidad de paginas del libro a imprimir: "))
valor = (paginas * 3.2) + 500
if paginas < 300:
    print("El costo del libro seria de:", valor)
elif paginas >= 300 and paginas < 600:
    valor = valor + 200
    print("El costo del libro seria de:", valor)
else:
    valor = valor + 536
    print("El costo del libro seria de:", valor)
    
#Ejercicio 6

kilometros = int(input("Ingrese la cantidad de kilometros de su viaje: "))
if kilometros > 0 and kilometros <= 10:
    valor = kilometros * 30
    if valor < 250:
        valor = 250
elif kilometros > 10:
    valor = kilometros * 20
else:
    print("Error, dato no valido")
print("El valor del viaje es de:", valor)
"""
#Ejercicio 7

fecha = int(input("Ingrese un año para saber si es o no bisiesto: "))
if fecha % 4 == 0:
    if fecha % 100 == 0:
        print("El año no es bisiesto.")
    else:
        print("El año es bisiesto.")
else:
    print("El año es bisiesto.")










    
    