'''Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.'''
'''print(now.year()) def calculadora_edad(año edad = now.year''' 
    
from datetime import date
#Día actual
today = date.today()
print(today)
#Date
print("El año actual es {}".format(today.year))
anoactual = today.year
born = int(input('Introduzca su año de nacimiento '))
edad = anoactual - born
print(edad)