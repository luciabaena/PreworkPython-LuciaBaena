'''Ejercicio 18: Contador de Palabras
Ejercicios Introducción a Python: Enunciados 3
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''

oracion = input("Ingrese una oracion: ")
palabras = oracion.split()
print(len(palabras))