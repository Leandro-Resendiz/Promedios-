""" Programa que toma las tres calificaciones de un estudiante y diga el promedio final del curso.
    Teniendo en cuenta que la primera y segunda calificación tienen el valor del 30% de la calificación final. 
    La tercera calificación tendrá el valor del 40% """


def calcularPromedio(calificacion1, calificacion2, calificacion3):
    return (calificacion1*0.3)+(calificacion2*0.3)+(calificacion3*0.4)


calificacion1 = float(input("Ingresa tu primer calificación: "))
calificacion2 = float(input("Ingresa tu segunda calificación: "))
calificacion3 = float(input("Ingresa tu tercera calificación: "))


promedioFinal = calcularPromedio(calificacion1, calificacion2, calificacion3)

print("El promedio final del estudiante es: ", round(promedioFinal, 2))
