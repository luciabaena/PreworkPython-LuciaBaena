#Ejercicio 10: Determinar el Día de la Semana
#Escribe un programa que determine el día de la semana correspondiente a un
#número ingresado por el usuario (1 para lunes, 2 para martes, etc.).

def diasemana(numero):
    if numero > 7 or numero <= 0:
        print('Numero invalido, deber ser menor a 7 y positivo')
    elif numero == 1:
            print('El dia es lunes')
    elif numero == 2:
        print('El dia es martes')
    elif numero == 3:
        print('El dia es miercoles')
    elif numero == 4:
         print('El dia es jueves')
    elif numero == 5:
        print('El dia es viernes')
    elif numero == 6:
        print('El dia es sabado')
    else:
        print('El dia es domingo')
n=int(input('Introduce tu numero '))    
diasemana(n)
        
        
'''def diasemana(numero):''' '''contador = 0'''


  
