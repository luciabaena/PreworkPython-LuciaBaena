#Ejercicio 6: Verificación de Palíndromo
#Crea un programa que verifique si una palabra ingresada por el usuario es un
#palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).



#Ejercicio 7: Calculadora Simple
#Crea un programa que realice operaciones aritméticas simples (suma, resta,
#multiplicación, división) según la elección del usuario.

def calculadora (numero1, numero2, operacion):
    if operacion == 'multiplicacion':
        total = numero1 * numero2
    else:
        if operacion == 'division':
            total = numero1 / numero2 
        else:
            if operacion == 'suma':
                total = numero1 + numero2
            else:
                total = numero1 - numero2

    return total

operacion = input('Elija entre multiplicacion, division, suma o resta introduciendo la operacion a realizar ')
print(operacion)
number11 = int(input('Introduce un numero '))
number2 = int(input('Introduce un numero '))
resultado = calculadora(number11,number2,operacion)
print(resultado)

