'''Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.'''
precio = float(input('Introduce el precio '))
rebaja = float (input('Introduce el descuento '))/100
precio_final = precio * (1-rebaja)
print(precio_final)