#Ejercicio 9: Conversor de Divisas
#Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
def conversoraeuros(dollar, cambio):
    euro = dollar / cambio
    totally = round(euro,2) 
    print('El total en euros es', totally)
dolr=float(input('Introduce dollars '))
iuro=float(input('Introduce a cuanto esta el cambio '))
total = conversoraeuros(dolr, iuro)
