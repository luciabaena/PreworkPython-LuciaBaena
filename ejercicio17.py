'''Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.'''

milles = float(input('Introduce el numero de millas '))
cambio = 1.60934
km = round(milles/cambio, 2)
print(km)