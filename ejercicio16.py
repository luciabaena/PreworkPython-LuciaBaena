'''Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())
	# adding the element
	lst.append(ele) 

print(lst)
contador_par = 0
contador_impar = 0
for numero in lst:
    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print(f'Total numero pares {contador_par} y de impares {contador_impar}')