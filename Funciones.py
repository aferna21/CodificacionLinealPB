import math
import numpy as np
import itertools 


################################################################
#                                                              #
#                   FUNCIONES DE CODIFICACION                  #
#                                                              #
################################################################

# Calcula cuántos elementos diferentes hay en una lista.
# -Parámetros: 
#               lista: lista de la que quieres saber su número de elementos.
# -Return: el número de elementos diferentes.
def getNumeroDeElementosDiferentesEnLista(lista):
    set_sin_repeticiones = set(lista)
    return len(set_sin_repeticiones)


# Calcula la mínima longitud en bloque.
# -Parámetros:
#               alfabeto: alfabeto utilizado
#               num_elementos: número de elementos diferentes que tiene el mensaje (módulo)
# -Return: la mínima longitud binaria en bloque.
def calculaMinimaLongitudEnBloque(alfabeto, num_elementos):
    longitud_alfabeto = len(alfabeto)
    minima_longitud = math.ceil(math.log(longitud_alfabeto, num_elementos)) 
    return minima_longitud


# Transforma un número decimal en otro con cualquier base. 
# -Parámetros:
#               -numero: numero decimal el cual se quiere transformar.
#               -base: base a la que se quiere transformar el número.
#-Return: una lista cuyos elementos son los dígitos que forman el número transformado.
def devuelveNumeroEnBase(numero, base):
    salida = []
    while numero > base:
        tupla = divmod(numero, base)
        resto = tupla[1]
        numero = tupla[0]
        salida.append(resto)
    
    if numero == base:
        salida.append(0)
        salida.append(1)
    else:
        salida.append(numero)
    salida.reverse()
    return salida


# Rellena una lista inicial con ceros a la izquierda hasta que sea de un determinado tamaño
# -Parámetros:
#               -lista_inicial: lista la cual quieres hacer más grande
#               -tam: tamaño que quieres que alcance lista_inicial
# -Return: lista rellena de ceros por la izquierda con tamaño tam.
def rellenaListaConCeros(lista_inicial, tam):
    cero = 0
    if tam == 1:
        lista_inicial = [cero] + lista_inicial
    else:
        while len(lista_inicial) != tam:
            lista_inicial = [cero] + lista_inicial
    return lista_inicial


# Busca la posición de un símbolo en un alfabeto y la transforma en una determinada base con su correspondiente tamaño.
# -Parámetros:
#               -simbolo: símbolo a codificar
#               -alfabeto: alfabeto el cual contiene el simbolo
#               -num_elementos: base a la que se quiere transformar la posicion del simbolo en el alfabeto
# -Return: la posición del símbolo en el alfabeto en base num_elementos con su correspondiente longitud. 
def codificaSimbolo(simbolo, alfabeto, num_elementos):
    indice = alfabeto.index(simbolo)
    lista_binaria = devuelveNumeroEnBase(indice, num_elementos)
    minima_longitud = calculaMinimaLongitudEnBloque(alfabeto, num_elementos)
    lista_binaria_completa = rellenaListaConCeros(lista_binaria, minima_longitud)
    return lista_binaria_completa



# Función que te devuelve la lista de posiciones que ocupa cada símbolo
# de un mensaje dentro de un alfabeto
# -Parámetros:
#               -mensaje: mensaje del cual se quieren saber las posiciones en el alfabeto
#               -alfabeto: alfabeto que contiene los símbolos del mensaje
# -Return: la lista de posiciones
def fromMensajeToListaPosiciones(mensaje, alfabeto):
    lista_posiciones = []
    for i in mensaje:
        lista_posiciones.append(alfabeto.index(i))
    return lista_posiciones

# Unifica una lista compuesta por listas.
#-Parámetros: 
#               -lista: lista a unificar
#-Return: la lista "lista" unificada. 
def unificaLista(lista):
    return list(itertools.chain.from_iterable(lista))



# Codifica una expresión completa símbolo a símbolo mediante la función codificaSimbolo
# -Parámetros:
#               -expresion: expresion a codificar
#               -alfabeto: alfabeto en el cual se encuentran los símbolos de expresion
#               -num_elementos: número de elementos (módulo) que codificarán a la expresión
# -Return: lista que forma la expresión codificada.
def codificaExpresion(expresion, alfabeto, num_elementos):
    expresion_codificada = []
    for simbolo in expresion:
        simbolo_codificado = codificaSimbolo(simbolo, alfabeto, num_elementos)
        expresion_codificada.append(simbolo_codificado)
    
    print(f"\n-PASO 2:\n lista_codificacion_alfabeto: {expresion_codificada}")
    return unificaLista(expresion_codificada)

# Divide una lista en partes con una longitud determinada. Si la división no resulta exacta,
# la última parte será el resto de la división de la longitud de la lista entre la longitud de cada parte.
# -Parámetros: 
#               -lista: lista la cual se quiere dividir en partes
#               -longitud_parte: cuánto ha de medir cada una de las partes en las que se divide la lista
# -Return: la lista dividida
def divideListaConResto(lista, longitud_parte):
    lista_en_partes = []
    for _ in range(0, len(lista), longitud_parte):
        lista_en_partes.append(lista[:longitud_parte])
        del lista[:longitud_parte]
    return lista_en_partes


# Multipica dos matrices como si la segunda tuviese ligada a ella la matriz identidad.
# -Parámetros: 
#               -matriz1: primer factor de la multiplicación
#               -matriz2: segundo factor de la multiplicación. Se trabajará con él como si tuviese ligada
#                         la matriz identidad correspondiente
#               -num_elementos: módulo en el que estará el resultado de la multiplicación
# -Return: el resultado de multiplicar la matriz1 con la matriz2_sinidentidad h
def multiplicaMatricesAniadiendoIdentidad(matriz1, matriz2_sin_identidad, num_elementos):
    matrices_multiplicadas = np.array(matriz1).dot(matriz2_sin_identidad)
    resultado_completo = np.append(matriz1, matrices_multiplicadas)
    return devuelveEnModulo(resultado_completo, num_elementos)


# Transforma una lista a un módulo determinado.
# -Parámetros:
#               -lista: lista a transformar
#               -num_elementos: módulo al que se quiere pasar lista
# -Return: lista en módulo num_elementos.
def devuelveEnModulo(lista, num_elementos):
    salida = []
    for i in lista:
        salida.append(i%num_elementos)
    return salida



# Método que codifica una expresión la cual debe estar en la forma correspondiente a través de una matriz. Primero divide la expresión entre las filas de esa matriz
# (pudiendo quedar un resto). Luego va multiplicando cada parte de la expresión por esa matriz, manteniendo el módulo correspondiente.
# -Parámetros:
#               -expresion: expresion a codificar
#               -matriz: matriz a través de la cual se codifica
#               -num_elementos: módulo en el que estará el resultado
# -Return: la expresión codificada.
def codificaExpresionEnMatriz(expresion, matriz, num_elementos):
    filas_matriz = len(matriz)
    print("\n-PASO 3.a:")
    expresion_en_trozos = divideListaConResto(expresion, filas_matriz)
    print(f"La lista dividida es: {expresion_en_trozos}")
    expresion_codificada = []
    for i in range(len(expresion_en_trozos) - 1):
        multiplicacion = multiplicaMatricesAniadiendoIdentidad(expresion_en_trozos[i], matriz, num_elementos)
        expresion_codificada.append(multiplicacion)

    if len(expresion_en_trozos) % filas_matriz != 0:
        expresion_codificada.append(expresion_en_trozos[-1])
    else:
        multiplicacion = multiplicaMatricesAniadiendoIdentidad(expresion_en_trozos[-1], matriz, num_elementos)
        expresion_codificada.append(multiplicacion)
    print(f"\n-PASO 3.b:\n lista_mensaje_codificado es: {expresion_codificada}")
    return unificaLista(expresion_codificada)


# Método que codifica una expresión en crudo.
# -Parámetros: 
#               -alfabeto: alfabeto que contendrá los símbolos del mensaje a codificar.
#               -matriz: matriz a través de la cual se realizará la segunda codificación
#               -numero_de_elementos: módulo de la expresión codificada (elementos diferentes en la matriz)
#               -mensaje: mensaje a codificar
# -Return: mensaje codificado.
def codifica(alfabeto, matriz, numero_de_elementos, mensaje):
    print(f"\n-PASO 1\nLa mínima longitud en bloque es: {calculaMinimaLongitudEnBloque(alfabeto, numero_de_elementos)}")
    expresion = codificaExpresion(mensaje, alfabeto, numero_de_elementos)
    expresion_codificada_en_matriz = codificaExpresionEnMatriz(expresion, matriz, numero_de_elementos)
    return(expresion_codificada_en_matriz)
    
################################################################
#                                                              #
#                  FUNCIONES DE DECODIFICACION                 #
#                                                              #
################################################################
    

# Coge una lista troceada en partes y forma otra con los determinados primeros dígitos de cada parte 
# -Parámetros:
#               -lista: lista troceada de la cual se quieren extraer los primeros dígitos de cada parte
#               -digitos_reales: el número de primeros dígitos que se quieren extraer de cada parte de la lista
# -Return: lista cuyos elementos son sublistas de la original.
def fromListaDividaASecuencias(lista, digitos_reales):
    secuencias = []
    for i in lista:
        secuencias.append(i[0:digitos_reales])
    return secuencias


# Transforma cualquier número en cualquier base a decimal
# -Parámetros:
#               -numero: numero a transformar
#               -base: base en la que se encuentra el número
# -Return: el número numero en base base en base decimal
def fromBaseNToDecimal(numero, base):
    numero.reverse()
    decimal = 0
    for i in range(len(numero)):
        decimal += numero[i] * (base ** i)
    return decimal


# Transforma los números de una lista de cualquier base a base decimal
# -Parámetros:
#               -lista_base_n: lista que contiene números en base no decimal
#               -base: base en la que se encuentran los números de la lista
# -Return: el número numero en base base en base decimal
def fromListaBaseNToListaDecimal(lista_base_n, base):
    lista_decimal = []
    for i in lista_base_n:
        lista_decimal.append(fromBaseNToDecimal(i, base))
    return lista_decimal


# Devuelve el mensaje a partir de una lista que contiene números (posiciones del alfabeto).
# -Parámetros:
#               -alfabeto: alfabeto del cual se quiere extaer el mensaje
#               -lista: lista que contiene las posiciones de las letras del mensaje
# -Return: mensaje que corresponde a la lista.
def getMensajeFromListaPosiciones(alfabeto, lista):
    mensaje = ""
    for i in lista:
        mensaje += str(alfabeto[i])
    return mensaje



# Decodifica un mensaje.
# -Parámetros:  
#               -alf: alfabeto que contiene todos los posible símbolos del mensaje
#               -matriz: matriz por la que se codificó el mensaje
#               -num_elementos: módulo del mensaje codificado
#               -lista: mensaje codificado
# -Return: mensaje decodificado
def decodifica(alf, matriz, num_elementos, lista):
    digitos_totales_secuencia = len(matriz) + len(matriz[0])
    digitos_reales_secuencia = len(matriz)
    secuencia_dividida = divideListaConResto(lista, digitos_totales_secuencia)
    print(f"\nPASO 2:\n lista_mensaje_codificado: {secuencia_dividida}")
    resto = []
    if len(secuencia_dividida[-1]) != digitos_totales_secuencia:
        resto = secuencia_dividida[-1]
        del secuencia_dividida[-1]
    secuencias = fromListaDividaASecuencias(secuencia_dividida, digitos_reales_secuencia)
    secuencias.append(resto)
    print(f"\nPASO 3:\n lista_codificacion_alfabeto: {secuencias}")
    secuencias_unificadas = unificaLista(secuencias)
    minima_longitud_binaria = calculaMinimaLongitudEnBloque(alf, num_elementos)
    primera_codificacion_dividida = divideListaConResto(secuencias_unificadas, minima_longitud_binaria)
    print(f"\nPASO 4:\nlista_codificacion_alfabeto: {primera_codificacion_dividida}")
    lista_posiciones_alfabeto = fromListaBaseNToListaDecimal(primera_codificacion_dividida, num_elementos)
    print(f"\nPASO 5:\nmensaje_decodificado_numero: {lista_posiciones_alfabeto}")
    mensaje_final = getMensajeFromListaPosiciones(alf, lista_posiciones_alfabeto)
    print(f"\nPASO 6:\nMensaje final decodificado: {mensaje_final}")
    return mensaje_final