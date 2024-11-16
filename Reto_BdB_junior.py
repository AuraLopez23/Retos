def filtrado_num(lista, S):
    procesados = []
    for num in lista:
        # Filtrar los dígitos menores que S
        filtrados = [digito for digito in str(num) if int(digito) < S]
        # Solo agregar al resultado si hay dígitos válidos
        if filtrados:
            new_num = int("".join(filtrados))
            procesados.append(new_num)
    return procesados

# Ejemplo de uso
numbers = [123, 61, 56, 789, 345, 1, 0]
S = 2
resultado = filtrado_num(numbers, S)
print("Resultado del reto 1:",resultado)

#-------------------------------------------------
#CHALLENGE 2

def numeros_cuadrados(lista_2 , SS):
    resultado_1 = [0] * len(lista_2)  #Se genera una lista del mismo tamaño de la lista de entrada
    left = 0
    right = len(lista_2) - 1
    indice = len(lista_2) - 1
# A continuacion se realiza un recorrido de la lista para evaluar qué números cumplen la condición
    while left <= right:
        left_v = abs(lista_2[left])
        right_v = abs(lista_2[right])

        if left_v > right_v:
            square = left_v ** 2
            left += 1
        else:
            square = right_v ** 2
            right -= 1
# Con el cuadrado hallado se verifica la condicion de que sea igual o menor a SS
        if square <= SS:
            #Asigna el valor resutado a una posición de la lista de resultado_1
            resultado_1[indice] = square
            indice -= 1

    return resultado_1[indice + 1:]


lista_2 = [-8, -3, 0, -2, 2, 4, 5, 6, 8]
SS = int(str(S) + str(S))
print("SS =",SS)
res_reto2 = numeros_cuadrados(lista_2,SS)
print("Resultado del reto 2:",res_reto2)

#------------------------------------------------------------------------------------
#CHALLENGE 3

def minimo_cambio(monedas):
    monedas.sort()  #Se ordenan las monedas
    #Según las pistas, se inicia por el valor minimo de cambio
    cambio_minimo = 1

    for moneda in monedas:
        if moneda > cambio_minimo:
            break
        cambio_minimo += moneda

    return cambio_minimo


#Lista de monedas para evaluar el minimo cambio
monedas = [1, 2, 4, 9]

Resultado_reto3= minimo_cambio(monedas)
print("Resultado de reto 3:", Resultado_reto3)