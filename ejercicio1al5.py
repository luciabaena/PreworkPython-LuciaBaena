#Ejercicio 1: Conversor de Temperatura
#Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.

def conversor_temperature (Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit
USA_temperature = conversor_temperature(0)
print(USA_temperature)

#Ejercicio 2: Calculadora de Propina
#Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo 
#una propina del 15% sobre el total de la cuenta.

hola = 2
creo = 4
to = hola / creo 
print(creo)

def total_bill(menu, tip):
    suma = 0 
    total = 0 
    for order in menu:
        suma += order *(1+tip)
    return suma
gasto = total_bill([1, 2, 3, 4],15/100)
print(gasto)

#Ejercicio 3: Verificación de Edad Escribe un programa que solicite la edad de un usuario y determine si es mayor de
#edad (mayor o igual a 18 años) o no.
def adulthood (age):
    adult = 18
    if age < adult:
        print ('You are not old enough')
    else:
        print ('Yay! You can drive')

name = adulthood(17)

#Ejercicio 4: Contador de Vocales Crea un programa que cuente el número de vocales en una palabra ingresada por el
#usuario.
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador
cadena = 'as'
contar = contar_vocales(cadena)
print(contar)

#Ejercicio 5: Suma de Números Pares
#Escribe un programa que calcule la suma de todos los números pares del 1 al 100.

print('Introduce el numero inicial del rango')
i = int(input())
print('Introduce el numero final del rango')
f = int(input())
suma = 0
while i <=f:
    if i % 2 == 0:
        suma = suma + i
    i +=1

print(suma)