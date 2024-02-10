'''Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.'''

año = int(input('Introduce un año '))

if año % 4 == 0:
    bisiesto = True
    if año % 100 == 0  and año % 400 == 0:
        bisiesto = True
    elif año % 100 == 0 and año % 400 != 0:
        bisiesto = False
else:
    bisiesto = False

print(bisiesto)
        



