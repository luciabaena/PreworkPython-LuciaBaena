'''Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.'''

def area(longitud, ancho):
    area = round(float(longitud * ancho),2)
    print(f"El area es {area}")

long = float(input('Introduce el largo '))
wide = float(input ('Introduce el ancho ')) 
area(long, wide)  

