'''Ejercicio 15: Conversor de Tiempo
Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''

minutos = int(input('Introduce los minutos '))
horas = 0
while minutos >= 60:
    minutos -= 60
    horas += 1

print(f'El tiempo total es {horas} horas y {minutos} minutos')