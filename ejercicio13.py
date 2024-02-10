'''Ejercicio 13: Verificación de Número Primo
Escribe un programa que determine si un número ingresado por el usuario es primo
o no.'''

numero = int(input('Introduce numero'))
es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        
        break
print(f'El resultado es que primo es {es_primo}')


