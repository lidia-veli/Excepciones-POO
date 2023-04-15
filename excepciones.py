# IMPORTACIONES ----------------------------------------------------------------------------------------
import re
from enum import Enum
class Genero(Enum):
    M = "o"
    F = "a"
    NB = "e"

# VARIABLES GLOBALES ----------------------------------------------------------------------------------------
vacio = ["", " "]
dict_cuentas_existentes = {'vicente@eni.es':['Vicente', Genero.M], 
                           'julia@telefonica.es':['Julia', Genero.F], 
                           'alex@gmail.com':['Alex', Genero.NB] }


# FUNCIONES ----------------------------------------------------------------------------------------
def caracteres_validos(s):
    '''Función que verifica si una cadena de texto tiene el formato de un correo electrónico'''
    if re.search('.*@.*\..*', s):
        return True
    else:
        return False

def pedir_entrada():
    '''Funcion para que el usuario introduzca su correo electrónico.'''
    return str(input("Introduzca su correo electrónico: "))


def entrada_no_vacia(entrada):
    ''''Funcion para verificar que la cadena de texto no es vacía.'''
    if entrada in vacio:
        raise ValueError("Entrada no válida.")
    else:
        return entrada


def formato_correcto(entrada):
    '''Funcion que verifica si la cadena de texto tiene el formato de texto requerido de un correo electrónico.'''
    if caracteres_validos(entrada) is False:
        raise ValueError("Formato no válido. Una dirección de correo debe tener el formato: xxx@xxx.xx")
    else:
        return entrada


def correo_asociado_a_cuenta(entrada):
    '''Función para verificaar si el correo introducido está asociado a alguna cuenta activa o no.'''
    if entrada not in dict_cuentas_existentes:
        raise ValueError("Este correo no está asociado a ninguna cuenta.")
    else:
        return entrada


def main():
    '''Función que modeliza el ejercicio'''
    intentos = 0
    while True:
        if intentos <=2: # si se han realizado más de 2 intentos fallidos, se bloquea
            entrada = pedir_entrada()
            intentos += 1
            try:
                entrada = entrada_no_vacia(entrada)
                entrada = formato_correcto(entrada)
                entrada_correo = correo_asociado_a_cuenta(entrada)
            except ValueError as e: # si hay error, se repite el bucle
                print(e)
                continue
            else: # si no hay error, se accede
                terminacion_genero = dict_cuentas_existentes[entrada_correo][1].value
                nombre_usuario = dict_cuentas_existentes[entrada_correo][0]
                print( f"¡Bienvenid{terminacion_genero}, {nombre_usuario}!")
                break
        else:
            print('Cuenta bloqueada. Demasiados intentos fallidos.')
            break
    # si hemos salido del bucle, es porque el correo es válido
    return


# CÓDIGO EJECUTABLE ----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
