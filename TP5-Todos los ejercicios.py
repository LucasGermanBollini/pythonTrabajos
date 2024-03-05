#Ejercicio 1
menoresEdad = 0
mayoresEdad = 0
promedio = 0
n = int(input("Ingrese una edad entre 0 y 100, y para terminar ingrese -1: "))

while n != -1:
    if n >= 0 and n < 18:
        menoresEdad = menoresEdad + 1
        promedio = n + promedio
    elif n >= 18 and n <= 100:
        mayoresEdad = mayoresEdad + 1
        promedio = n + promedio
    else:
        print("Error, edad no valida.")

    n = int(input("Ingrese una edad: "))
print("Son menores de edad:",menoresEdad,"y son mayores de edad:",mayoresEdad, ", y el promedio es de",promedio / (mayoresEdad+menoresEdad))

#Ejercicio 2
aplazado = 0
desaprobados = 0
aprobados = 0

legajo = int(input("Ingrese el numero de legajo: "))

while legajo != -1:
    nota = int(input("Ingrese la nota final del alumno: "))
    if nota == 1:
        aplazado = aplazado + 1
        print("El alumno aplazo la materia y su numero de legajo es:", legajo)
    elif nota >= 2 and nota < 4:
        desaprobados = desaprobados + 1
        print("El alumno desaprobo la materia y su numero de legajo es:", legajo)
    elif nota >= 4 and nota <= 10:
        aprobados = aprobados + 1
        print("El alumno aprobo la materia y su numero de legajo es:", legajo)
    else:
        print("Error dato no valido.")
    legajo = int(input("Ingrese el numero de legajo: "))

    
print("La cantidad de alumnos aplazados son:", aplazado, "La cantidad de alumnos desaprobados son:", desaprobados, "La cantidad de alumnos aprobados es de:",aprobados)

#Ejercicio 6

contador = 0
numero = int(input("Ingrese su numero entero: "))

if numero > 0:
    while numero >= 1:
        numero = numero / 10
        contador = contador + 1
elif numero < 0:
    while numero <= -1:
        numero = numero / 10
        contador = contador + 1

print(contador)

#Ejercicio 9
suma = 0
numero = int(input("Ingrese un numero entero: "))
while numero <= 0:
    numero = int(input("Ingrese un numero positivo distinto de 0: "))

while numero >= 1:
    if numero % 2 == 0:
        numero = numero - 1
        if numero > 0:
            print(numero)
    suma = numero + suma
    numero = numero - 2
    if numero > 0:
        print(numero)
    
    
    
print("La suma de los impares es de:",suma)


#Ejercicio 8

totalSalario = 0
cantidadSalario = 0
empleadosCantidadMayores = 0
categoria3sueldo = 0
legajoMayor = 0
sueldoMenor = 0
legajoMayorReal = 0
salarioCate3 = 0
salarioCate2 = 0
salarioCate1 = 0

empleados = int(input("Ingrese la cantidad de empleados de la empresa: "))
legajo = int(input("Ingrese el numero de legajo del empleado: "))
categoria = int(input("Ingrese la categoria del empleado (debe ser 1, 2 o 3): "))
while categoria  < 1 or categoria > 3:
    categoria = int(input("Error, ingrese la categoria del empleado (debe ser 1, 2 o 3): "))
salario = int(input("Ingrese la cantidad del sueldo del empleado: "))

while cantidadSalario < empleados:

    totalSalario = totalSalario + salario
    cantidadSalario = cantidadSalario + 1
    if cantidadSalario == 1:
        sueldoMenor = salario
    if salario > legajoMayor:
        legajoMayor = salario
        legajoMayorReal = legajo
    if salario > 200000:
        empleadosCantidadMayores = empleadosCantidadMayores + 1
    if salario < 50000 and categoria == 3:
        categoria3sueldo = categoria3sueldo + 1
    if salario < sueldoMenor:
        sueldoMenor = salario
    if categoria == 3:
        salarioCate3 = salarioCate3 + salario
    if categoria == 2:
        salarioCate2 = salarioCate2 + salario
    if categoria == 1:
        salarioCate1 = salarioCate1 + salario
    if cantidadSalario < empleados:
        legajo = int(input("Ingrese el numero de legajo del empleado: "))
        categoria = int(input("Ingrese la categoria del empleado (debe ser 1, 2 o 3): "))
        while categoria  < 1 or categoria > 3:
            categoria = int(input("Error, ingrese la categoria del empleado (debe ser 1, 2 o 3): "))
        salario = int(input("Ingrese la cantidad del sueldo del empleado: ")) 
    
print("El total de los salarios es de:",totalSalario)
print("La cantidad de empleados que ganan mas de $200.000 es de:",empleadosCantidadMayores)
print("Ganan menos de $50.000 y son de la tercera categoria:", categoria3sueldo)
print("Legajo del empleado que mas gana:",legajoMayorReal)
print("El sueldo mas bajo es de:",sueldoMenor)
print("El total de sueldos de la primera categoria es de:",salarioCate1)
print("El total de sueldos de la segunda categoria es de:",salarioCate2)
print("El total de sueldos de la tercera categoria es de:",salarioCate3)
print("El promedio de sueldos es de:",(totalSalario/cantidadSalario))
    

#Ejercicio 7
digitos = 0
nuevo = 0
n = 0
entero = int(input("Ingrese un numero entero: "))

while entero > 1:
    entero = entero / 10
    digitos = digitos + 1
entero =  entero * 10**digitos
print(entero)
print(digitos)
digitosNuevo = digitos

while n < digitosNuevo:
    nuevo = nuevo + ((entero % 10) * 10**(digitos-1))
    digitos = digitos - 1
    entero = entero // 10
    n = n + 1

print(int(nuevo))

#Ejercicio 4
primeroOpcionA = 0;primeroOpcionB = 0;tercero = 0;terceroB = 0;terceroReal = 0

cliente = int(input("Ingrese el numero de cliente: "))
factura = int(input("Ingrese el monto total de la factura: "))

primeroOpcionA = factura - (factura * 0.02)
primeraOpcionB = factura - 200
tercero = factura + 350
terceroB = factura + (factura * 0.1)
if tercero > terceroB:
    terceroReal = tercero
else:
    terceroReal = terceroB
    
print("Si paga los primeros diez dias, su factura sera del:",primeroOpcionA,"o",primeraOpcionB)
print("Si paga entre el dia 10 y el dia 20, su factura sera del:",factura)
print("Si paga luego de pasados los 20 dias, su factura sera de:",terceroReal)

#Ejercicio 8 (TP 3)
sumaPares = 0
contador = 0
sumaTotal = 0
numero = int(input("Ingrese numeros hasta que el programa pare: "))
while sumaPares < 100:
    if numero % 2 == 0:
        sumaPares = sumaPares + numero
        sumaTotal = sumaTotal + numero
    else:
        sumaTotal = sumaTotal + numero
    contador = contador + 1
    if sumaPares < 100:
        numero = int(input("Ingrese numeros hasta que el programa pare: "))
    

print(sumaTotal,contador)

#Ejercicio Factorial
total = 1
n = int(input("Ingrese un numero entero mayor a 0: "))
while n <= 0:
    n = int(input("Dato no valido, ingrese un numero entero mayor a 0: "))

while n > 1:
    total = total * n
    n = n - 1
print(total)

#Ejercicio 6
contador = 0
multiplicar = int(input("Ingrese el numero para multiplicar: "))
while contador < 12:
    contador = contador + 1
    print(contador * multiplicar)

#Ejercicio fechas

bisiesto = 0

dia = int(input("Ingrese el dia: "))
while dia < 1 or dia > 31:
    dia = int(input("Fecha no valida, ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
while mes < 1 or mes > 12:
    mes = int(input("Fecha no valida, ingrese el mes: "))           
año = int(input("Ingrese el año: "))
while año <= 0:
    año = int(input("Fecha no valida, ingrese el año: "))
    
diaSuma = int(input("Ingrese la cantidad de dias que desea sumar: "))

if año % 4 == 0:
    bisiesto = 1
    if año % 100 == 0:
        bisiesto = 0
        if año % 400 == 0:
            bisiesto = 1
else:
    bisiesto = 0
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if diaSuma + dia > 31:
        dia = dia + diaSuma - 31
        if mes == 12:
            año = año + 1
            mes = 1
        else:
            mes = mes + 1
    else:
        dia = dia + diaSuma

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if diaSuma + dia > 30:
        dia = dia + diaSuma - 30
        mes = mes + 1
    else:
        dia = dia + diaSuma
        
if mes == 2:
    if bisiesto == 1:
        if diaSuma + dia > 29:
            dia = dia + diaSuma - 29
            mes = mes + 1
        else:
            dia = dia + diaSuma
    if bisiesto == 0:
        if diaSuma + dia > 28:
            dia = dia + diaSuma - 28
            mes = mes + 1
        else:
            dia = dia + diaSuma
print(dia, mes, año)

#ejercicio 11

primo = int(input("Ingrese un numero entero: "))
primo2 = 0
variable = 2
if primo == 3 or primo == 5 or primo == 7:
    variable = 10
while variable < 9:
    if primo % variable == 0:
        primo2 = primo2 + 1
    variable = variable + 1
if primo2 > 0:
    print("El numero no es primo.")
else:
    print("El numero es primo.")

