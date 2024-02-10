#Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.

def mascorporal(peso, altura):
    IMC = peso / (altura*altura)
    print(IMC)

int1= float(input('Introduce tu peso '))
int2 = float(input('Introduce tu altura '))
resultado = mascorporal(int1, int2)


