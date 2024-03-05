#Ejercicio 1

#Variables
alumnosAprobados = 0
alumnosDesaprobados = 0
sumaNotas = 0
listaLegajo = []
listaNotas = []

#Inputs
legajo = int(input("Ingrese el numero de legajo del alumno: "))
nota = int(input("Ingrese la nota final del alumno: "))


#Condicionales
while legajo != -1:
    while nota < 1 or nota > 10:
        print("Error, nota invalida, debe ingresar un valor entre 1 y 10.")
        nota = int(input("Ingrese la nota final del alumno: "))
    if nota >= 4 and nota <= 10:
        alumnosAprobados = alumnosAprobados + 1
        sumaNotas = sumaNotas + nota
        listaNotas.append(nota)
        listaLegajo.append(legajo)
    if nota >= 1 and nota < 4:
        alumnosDesaprobados = alumnosDesaprobados + 1
        sumaNotas = sumaNotas + nota
        listaNotas.append(nota)
        listaLegajo.append(legajo)
    legajo = int(input("Ingrese el numero de legajo del alumno: "))
    if legajo != -1:
        nota = int(input("Ingrese la nota final del alumno: "))
    
#Calculos
cantidadNotas = alumnosAprobados + alumnosDesaprobados
promedio = sumaNotas / cantidadNotas
mejoresNotas = []

for i in range(0,len(listaNotas)-1):
    if listaNotas[i] > promedio:
        mejoresNotas.append(listaLegajo[i])
 
#Pantalla
print("La cantidad de alumnos que aprobaron es de",alumnosAprobados)
print("------------------------------------------------------------")
print("La cantidad de alumnos que desaprobaron es de",alumnosDesaprobados)
print("------------------------------------------------------------")
print("El promedio de todas las notas es de",promedio)
print("------------------------------------------------------------")
print("Las mejores notas fueron",mejoresNotas)