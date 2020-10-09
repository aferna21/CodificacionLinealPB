import Funciones
import numpy as np
from tkinter.filedialog import askopenfilename




alf="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ .,;¿?¡!_áéíóú()-0123456789ÁÉÍÓÚ"
alf_traduccion = "abcdefghijklmnñopqrstuvwxyz"

num_elementos = len(alf_traduccion)

print('¡Bienvenido al programa de codificación y decodificación lineal!')
print(f'Trabajaremos con el alfabeto "{alf}" y con un total de {num_elementos} elementos')

eleccion_problema = (int)(input("\n¿Qué desea hacer?\nPulse 1 para codificar.\nPulse 2 para decodificar\n"))

eleccion_input = (int)(input('Desea introducir la matriz (pulse 1) o cogerla de un archivo (pulse 2)\n'))

print("La forma que tiene la entrada es:\n1 0 0\n0 1 0\n0 0 1\nfin")
print("La entrada se cierra con un 'fin'\n")
matriz_string = None
if eleccion_input == 1:
    print("Inserte la matriz con la que quiere trabajar")
    matriz_string = input()
    matriz_string += str("\n")
    while matriz_string[-2] != "n":
        matriz_string += input()
        matriz_string += str("\n")
else:
    matriz_string = ""
    nombre_archivo = askopenfilename()
    with open(nombre_archivo) as f:
        for linea in f:
            matriz_string += str(linea)


def fromStringToMatriz(matriz):
    matriz_split = matriz.split('\n')
    matriz_split_integer = []
    columnas = len(matriz_split[0].split())
    for i in range(len(matriz_split) - 2):
        fila = matriz_split[i].split()
        for i in fila:
            matriz_split_integer.append(int(i))
    matriz_final = Funciones.divideListaConResto(matriz_split_integer, columnas)
    return np.array(matriz_final)

matriz = fromStringToMatriz(matriz_string)
matriz = Funciones.devuelveEnModulo(matriz, num_elementos)

if eleccion_problema == 1:
    mensaje = input("Introduzca el mensaje:\n")
    codificacion = Funciones.codifica(alf, matriz, num_elementos, mensaje)
    codificacion_adornada = Funciones.getMensajeFromListaPosiciones(alf_traduccion, codificacion)
    print(f"-PASO 4:\nFinalmente, el mensaje codificado es: {codificacion_adornada}")
else:
    mensaje_codificado_string = input("Introduzca el mensaje codificado\n")
    mensaje_codificado = Funciones.fromMensajeToListaPosiciones(mensaje_codificado_string, alf_traduccion)
    print(f"\n-PASO 1:\nlista_mensaje_codificado: {mensaje_codificado}")
    decodificacion = Funciones.decodifica(alf, matriz, num_elementos, mensaje_codificado)
    



